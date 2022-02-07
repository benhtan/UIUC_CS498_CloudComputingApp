import java.io.IOException;
import java.lang.Integer;
import java.util.*;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.input.KeyValueTextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

public class TopWords {
	public static class TextArrayWritable extends ArrayWritable {
		public TextArrayWritable() {
			super(Text.class);
		}

		public TextArrayWritable(String[] strings) {
			super(Text.class);
			Text[] texts = new Text[strings.length];
			for (int i = 0; i < strings.length; i++) {
				texts[i] = new Text(strings[i]);
			}
			set(texts);
		}
	}


	public static class WordCountMap extends Mapper<Object, Text, Text, IntWritable> {
		List<String> commonWords = Arrays.asList("the", "a", "an", "and", "of", "to", "in", "am", "is", "are", "at", "not");
		@Override
		public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
			String line = value.toString();
			StringTokenizer tokenizer = new StringTokenizer(line, " \t,;.?!-:@[](){}_*/");
			while (tokenizer.hasMoreTokens()) {
				String nextToken = tokenizer.nextToken();
				if (!commonWords.contains(nextToken.trim().toLowerCase())) {
					context.write(new Text(nextToken), new IntWritable(1));
				}
			}
		}
	}

	public static class WordCountReduce extends Reducer<Text, IntWritable, Text, IntWritable> {
		@Override
		public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
			int sum = 0;
			for (IntWritable val : values) {
				sum += val.get();
			}
			context.write(key, new IntWritable(sum));
		}
	}

	public static class TopWordsMap extends Mapper<Text, Text, NullWritable, TextArrayWritable> {
		private TreeSet<Pair<Integer, String>> countToWordMap = new TreeSet<Pair<Integer, String>>();

		@Override
		public void map(Text key, Text value, Context context) throws IOException, InterruptedException {
			Integer count = Integer.parseInt(value.toString());
			String word = key.toString();

			countToWordMap.add(new Pair<Integer, String>(count, word));
			if (countToWordMap.size() > 10) {
				countToWordMap.remove(countToWordMap.first());
			}
		}


		@Override
		// aggregate all map output into one reduce key
		protected void cleanup(Context context) throws IOException, InterruptedException {
			for (Pair<Integer, String> item : countToWordMap) {
				String[] strings = {item.second, item.first.toString()};
				TextArrayWritable val = new TextArrayWritable(strings);
				context.write(NullWritable.get(), val);
			}
		}
	}

	public static class TopWordsReduce extends Reducer<NullWritable, TextArrayWritable, Text, IntWritable> {
		private TreeSet<Pair<Integer, String>> countToWordMap = new TreeSet<Pair<Integer, String>>();

		@Override
		public void reduce(NullWritable key, Iterable<TextArrayWritable> values, Context context) throws IOException, InterruptedException {
			for (TextArrayWritable val : values) {
				Text[] pair = (Text[]) val.toArray();
				String word = pair[0].toString();
				Integer count = Integer.parseInt(pair[1].toString());

				countToWordMap.add(new Pair<Integer, String>(count, word));
				if (countToWordMap.size() > 10) {
					countToWordMap.remove(countToWordMap.first());
				}
			}

			for (Pair<Integer, String> item : countToWordMap) {
				Text word = new Text(item.second);
				IntWritable value = new IntWritable(item.first);
				context.write(word, value);
			}
		}
	}

	public static void main(String[] args) throws Exception {
		Configuration conf = new Configuration();
		FileSystem fs = FileSystem.get(conf);
		Path tmpPath = new Path("/w1/tmp");
		fs.delete(tmpPath, true);

		// creating a word count job
		Job jobA = Job.getInstance(conf, "wordcount");
		jobA.setOutputKeyClass(Text.class);
		jobA.setOutputValueClass(IntWritable.class);

		jobA.setMapperClass(WordCountMap.class);
		jobA.setReducerClass(WordCountReduce.class);

		FileInputFormat.setInputPaths(jobA, new Path(args[0]));
		FileOutputFormat.setOutputPath(jobA, tmpPath);

		jobA.setJarByClass(TopWords.class);
		jobA.waitForCompletion(true);

		// creating a top words job
		Job jobB = Job.getInstance(conf, "topwords");
		jobB.setOutputKeyClass(Text.class);
		jobB.setOutputValueClass(IntWritable.class);

		jobB.setMapOutputKeyClass(NullWritable.class);
		jobB.setMapOutputValueClass(TextArrayWritable.class);

		jobB.setMapperClass(TopWordsMap.class);
		jobB.setReducerClass(TopWordsReduce.class);
		jobB.setNumReduceTasks(1);

		FileInputFormat.setInputPaths(jobB, tmpPath);
		FileOutputFormat.setOutputPath(jobB, new Path(args[1]));


		jobB.setInputFormatClass(KeyValueTextInputFormat.class);
		jobB.setOutputFormatClass(TextOutputFormat.class);

		jobB.setJarByClass(TopWords.class);
		System.exit(jobB.waitForCompletion(true) ? 0 : 1);
	}
}

class Pair<A extends Comparable<? super A>, B extends Comparable<? super B>> implements Comparable<Pair<A, B>> {
	public final A first;
	public final B second;

	public Pair(A first, B second) {
		this.first = first;
		this.second = second;
	}

	public static <A extends Comparable<? super A>, B extends Comparable<? super B>> Pair<A, B> of(A first, B second) {
		return new Pair<A, B>(first, second);
	}

	@Override
	public int compareTo(Pair<A, B> o) {
		int cmp = o == null ? 1 : (this.first).compareTo(o.first);
		return cmp == 0 ? (this.second).compareTo(o.second) : cmp;
	}

	@Override
	public int hashCode() {
		return 31 * hashcode(first) + hashcode(second);
	}

	private static int hashcode(Object o) {
		return o == null ? 0 : o.hashCode();
	}

	@Override
	public boolean equals(Object obj) {
		if (!(obj instanceof Pair))
			return false;
		if (this == obj)
			return true;

		return equal(first, ((Pair<?, ?>) obj).first) && equal(second, ((Pair<?, ?>) obj).second);
	}

	private boolean equal(Object o1, Object o2) {
		return o1 == o2 || (o1 != null && o1.equals(o2));
	}

	@Override
	public String toString() {
		return "(" + first + ", " + second + ")";
	}
}