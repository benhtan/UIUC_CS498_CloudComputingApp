# Fetch ubuntu 18.04 LTS docker image
FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive 
#[DEPRECATED] Make a copy of ubuntu apt repository before modifying it. 
#RUN mv /etc/apt/sources.list /sources.list
#[DEPRECATED] Now change the default ubuntu apt repositry, which is VERY slow, to another mirror that is much faster. It assumes the host already has created a sources.list.
#COPY sources.list /etc/apt/sources.list
COPY WordCount.java /etc/apt/WordCount.java
COPY TopWords.java /etc/apt/TopWords.java

#uncomment this line to find the fastest ubuntu repository at the time. Probably overkill, so disabling for now
#Note that this functionality is untested and might need debugging a bit.

# Update apt, and install Java + curl + wget on your ubuntu image.
RUN \
  apt-get update && \
  apt-get install -y curl vim wget expect git zip unzip && \
  apt-get install -y openjdk-8-jdk 

RUN \
  apt-get install -y python3 
  # && \
  #apt-get install -y python3-pip

ENV JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64
RUN curl -s "https://archive.apache.org/dist/hadoop/core/hadoop-2.9.2/hadoop-2.9.2.tar.gz" | tar -xz -C /usr/local/
RUN cd /usr/local && ln -s ./hadoop-2.9.2 hadoop


ENV HADOOP_PREFIX /usr/local/hadoop
ENV HADOOP_COMMON_HOME /usr/local/hadoop
ENV HADOOP_HDFS_HOME /usr/local/hadoop
ENV HADOOP_MAPRED_HOME /usr/local/hadoop
ENV HADOOP_YARN_HOME /usr/local/hadoop
ENV HADOOP_CONF_DIR /usr/local/hadoop/etc/hadoop
ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop
ENV HADOOP_CLASSPATH $JAVA_HOME/lib/tools.jar
ENV PATH="/usr/local/hadoop/bin:${PATH}"

RUN sed -i "/^export JAVA_HOME/ s:.*:export HADOOP_PREFIX=/usr/local/hadoop HADOOP_HOME=/usr/local/hadoop\n:" $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh
RUN sed -i '/^export HADOOP_CONF_DIR/ s:.*:export HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop/:' $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh


RUN chmod a+rwx -R /usr/local/hadoop/
#COPY autosu /usr/local/bin
#RUN chmod 777 /usr/local/bin/autosu
#RUN adduser hadoopuser --disabled-password --gecos ""
#RUN echo 'hadoopuser:hadooppass' | chpasswd

# Download and setup Apache Spark
RUN curl -s "https://archive.apache.org/dist/spark/spark-2.2.1/spark-2.2.1-bin-hadoop2.7.tgz" | tar -xz -C /usr/local/
RUN ln -s /usr/local/spark-2.2.1-bin-hadoop2.7 /usr/local/spark

ENV SPARK_HOME /usr/local/spark
ENV PATH="/usr/local/spark/bin:${PATH}"
RUN chmod a+rwx -R /usr/local/spark/

# Make vim nice
RUN echo "set background=dark" >> ~/.vimrc

ENV PYSPARK_PYTHON=python3