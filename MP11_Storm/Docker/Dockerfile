FROM ubuntu:18.04

ARG STORM_VERSION=apache-storm-1.2.4
ARG STORM_DOWNLOAD_URL=https://archive.apache.org/dist/storm/$STORM_VERSION/$STORM_VERSION.tar.gz

ARG REDIS_VERSION=redis-5.0.7
ARG REDIS_DOWNLOAD_URL=http://download.redis.io/releases/$REDIS_VERSION.tar.gz

ENV DEBIAN_FRONTEND noninteractive
RUN \
  apt-get update; \
  apt-get install -y --no-install-recommends \
  	vim maven expect zip unzip openjdk-8-jdk git \
  python python3-pip python3-dev python3-setuptools; \
  cd /usr/local/bin; \
  ln -s /usr/bin/python3 python; \
  rm -rf /var/cache/apt /var/lib/apt/lists

# Descript this!
RUN set -ex; \
  \
  buildDeps=' \
  	wget \
	gcc \
	make \
	python-pip python-setuptools python-dev \
  '; \
  apt-get update; \
  apt-get install -y --no-install-recommends $buildDeps; \
  rm -rf /var/lib/apt/lists/*; \
  \
  cd /usr/local; \
  wget -O $STORM_VERSION.tar.gz "$STORM_DOWNLOAD_URL"; \
  tar -xvf $STORM_VERSION.tar.gz; \
  ln -s ./$STORM_VERSION storm; \
  rm -rf /usr/local/$STORM_VERSION.tar.gz; \
  rm -rf /usr/local/storm/external; \
  chmod a+rwx -R /usr/local/storm; \
  \
  wget -O $REDIS_VERSION.tar.gz "$REDIS_DOWNLOAD_URL"; \
  tar -xvf $REDIS_VERSION.tar.gz; \
  ln -s ./$REDIS_VERSION redis; \
  rm -rf /usr/local/$REDIS_VERSION.tar.gz; \
  \
# https://github.com/docker-library/redis
# disable Redis protected mode [1] as it is unnecessary in context of Docker
# (ports are not automatically exposed when running inside Docker, but rather explicitly by specifying -p / -P)
# [1]: https://github.com/antirez/redis/commit/edd4d555df57dc84265fdfb4ef59a4678832f6da
  grep -q '^#define CONFIG_DEFAULT_PROTECTED_MODE 1$' /usr/local/redis/src/server.h; \
  sed -ri 's!^(#define CONFIG_DEFAULT_PROTECTED_MODE) 1$!\1 0!' /usr/local/redis/src/server.h; \
  grep -q '^#define CONFIG_DEFAULT_PROTECTED_MODE 0$' /usr/local/redis/src/server.h; \
  \
  make -C /usr/local/redis -j "$(nproc)"; \
  make -C /usr/local/redis install; \
  \
  rm /usr/local/redis; \
  rm -r /usr/local/$REDIS_VERSION; \
  \
  pip install storm redis; \
  pip3 install storm redis; \
  \
  apt-get purge -y --auto-remove $buildDeps

COPY entrypoint.sh /mp11/entrypoint.sh
COPY redis.conf /etc/redis/redis.conf

ENV JAVA_HOME "/usr/lib/jvm/java-1.8.0-openjdk-amd64"
ENV CLASS_PATH "/mp11/Jar/jedis.jar"
ENV STORM_HOME "/usr/local/storm"
ENV PATH "/usr/local/storm/bin:${PATH}"

COPY Jar/ /mp11/Jar/

RUN chmod a+rwx -R /mp11/

WORKDIR /mp11/solution

ENTRYPOINT ["/mp11/entrypoint.sh"]
