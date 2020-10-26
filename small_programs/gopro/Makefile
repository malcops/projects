CC=g++

.PHONY: test example

all: test example

test:
	$(CC) gopro.cpp test_gopro.cpp HTTPRequest.cpp -lgtest -lpthread -lcurl -o gtest

example:
	$(CC) gopro.cpp main.cpp HTTPRequest.cpp -o example -lcurl
