# Fetch ubuntu 18.04 LTS docker image
FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive
ENV PYSPARK_PYTHON=python3

RUN apt-get update && \
	apt-get install -y --no-install-recommends build-essential\
	expect git vim zip unzip wget openjdk-8-jdk wget sudo
RUN apt-get install -y python3 python3-pip python-dev build-essential python-pip
RUN cd /usr/local/bin; \
ln -s /usr/bin/python3 python;


################################################################################
####################   Spark stuff   ###########################################
################################################################################

# Download and install spark
RUN	cd /usr/local/ &&\
	wget "https://archive.apache.org/dist/spark/spark-2.4.1/spark-2.4.1-bin-hadoop2.7.tgz" &&\
	tar -xvzf spark-2.4.1-bin-hadoop2.7.tgz && \
	ln -s ./spark-2.4.1-bin-hadoop2.7 spark &&  \
	rm -rf /usr/local/spark-2.4.1-bin-hadoop2.7.tgz && \
	rm -rf /usr/local/spark/external && \
	chmod a+rwx -R /usr/local/spark/
RUN pip install numpy && pip3 install numpy

RUN echo "alias spark-submit='/usr/local/spark/bin/spark-submit'" >> ~/.bashrc

RUN cd /usr/local/spark/jars/ && \
	wget https://repos.spark-packages.org/graphframes/graphframes/0.7.0-spark2.4-s_2.11/graphframes-0.7.0-spark2.4-s_2.11.jar && \
 	chmod a+rwx graphframes-0.7.0-spark2.4-s_2.11.jar

ENV PYTHONPATH=:/usr/local/spark/jars/graphframes-0.7.0-spark2.4-s_2.11.jar

# Ensure spark log output is redirected to stderr
RUN cp /usr/local/spark/conf/log4j.properties.template /usr/local/spark/conf/log4j.properties

# Set relevant environment variables to simplify usage of spark
ENV SPARK_HOME /usr/local/spark
ENV PATH="/usr/local/spark/bin:${PATH}"
RUN chmod a+rwx -R /usr/local/spark/
