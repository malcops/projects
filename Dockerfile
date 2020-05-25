FROM debian:stable-slim

RUN dpkg --add-architecture i386 \
 && apt-get update \
 && apt-get install -y \
    build-essential \
    cmake \
    git \
    libzmq3-dev \
 && rm -rf /var/lib/apt/lists/*

RUN git clone -q https://github.com/google/googletest.git /googletest \
  && mkdir -p /googletest/build \
  && cd /googletest/build \
  && cmake .. && make && make install \
  && cd / && rm -rf /googletest
