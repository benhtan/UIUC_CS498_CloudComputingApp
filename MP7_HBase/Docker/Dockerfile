# Fetch ubuntu 18.04 LTS docker image
FROM ubuntu:18.04
ENV DEBIAN_FRONTEND noninteractive

RUN \
  apt-get update && \
  apt-get install -y --no-install-recommends net-tools vim sudo expect ssh openssh-server zip unzip wget openjdk-8-jdk gcc \
  python python-pip python-dev python-setuptools python3-pip python3-dev python3-setuptools && \
  apt-get autoremove -qq -y --purge && \
  apt-get clean && \
  rm -rf /var/cache/apt /var/lib/apt/lists && \
  cd /usr/local/ && \
  wget "https://archive.apache.org/dist/zookeeper/zookeeper-3.4.13/zookeeper-3.4.13.tar.gz" &&\
  tar -xvf zookeeper-3.4.13.tar.gz && \
  ln -s ./zookeeper-3.4.13 zookeeper &&  \
  rm -rf /usr/local/zookeeper-3.4.13.tar.gz && \
  mkdir /usr/local/zookeeper/data && \
  mkdir /usr/local/zookeeper/log && \
  rm -rf /usr/local/zookeeper/docs && \
  bash -c "echo '1' >> /usr/local/zookeeper/data/myid" && \
  chmod a+rwx -R /usr/local/zookeeper/ && \
  wget "https://archive.apache.org/dist/hbase/1.6.0/hbase-1.6.0-bin.tar.gz" && \
  tar -xzf hbase-1.6.0-bin.tar.gz && \
  rm -rf /usr/local/hbase-1.6.0-bin.tar.gz && \
  mv /usr/local/hbase-1.6.0* /usr/local/hbase && \
  rm -rf /usr/local/hbase/docs && \
  chmod a+rwx -R /usr/local/hbase/ && \
  pip install wheel happybase && \
  pip3 install wheel happybase && \
  cd /usr/local/ && \
  wget "https://archive.apache.org/dist/phoenix/phoenix-4.16.1/phoenix-hbase-1.6-4.16.1-bin.tar.gz" && \
  tar -xzf phoenix-hbase-1.6-4.16.1-bin.tar.gz && \
  rm -rf /usr/local/phoenix-hbase-1.6-4.16.1-bin.tar.gz && \
  mv /usr/local/phoenix-hbase-1.6-4.16.1* /usr/local/phoenix && \
  rm -rf /usr/local/phoenix/docs && \
  chmod a+rwx -R /usr/local/phoenix/ && \
  cp /usr/local/phoenix/phoenix-server-hbase-1.6-4.16.1.jar /usr/local/hbase/lib/

RUN cd /usr/local/bin; \
  ln -s /usr/bin/python3 python; 

ENV CLASSPATH=$CLASSPATH:/usr/local/phoenix/phoenix-client-hbase-1.6-4.16.1.jar

COPY zoo.cfg /usr/local/zookeeper/conf/zoo.cfg
COPY hbase-site.xml /usr/local/hbase/conf/hbase-site.xml
RUN wget -O /usr/local/hbase/conf/hbase-env.sh https://raw.githubusercontent.com/UIUC-CS498-Cloud/MP7_HBase_Template/main/Docker/hbase-env.sh

COPY auto* /usr/local/bin/
RUN chmod 777 /usr/local/bin/auto*
RUN adduser hadoopuser --disabled-password --gecos ""
RUN echo 'hadoopuser:hadooppass' | chpasswd && usermod -aG sudo hadoopuser
RUN sh -c "echo 'hadoopuser ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers"

ENV HBASE_HOME /usr/local/hbase
ENV PATH="/usr/local/hbase/bin:${PATH}"
ENV PATH="/usr/local/zookeeper/bin:${PATH}"
RUN chmod a+rwx -R /usr/local/hbase/


# Make vim nice
RUN echo "set background=dark" >> ~/.vimrc

