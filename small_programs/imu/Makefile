CC=g++

.PHONY: test example

all: test example

test:
	$(CC) IMU.cpp test_IMU.cpp -lgtest -lpthread -o gtest

example:
	$(CC) IMU.cpp main.cpp -o example
