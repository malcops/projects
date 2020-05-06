FROM debian:stable-slim

RUN dpkg --add-architecture i386 \
 && apt-get update \
 && apt-get install -y \
    build-essential \
    libzmq3-dev \
 && rm -rf /var/lib/apt/lists/*

