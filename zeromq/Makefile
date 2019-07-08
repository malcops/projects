CC=g++
CFLAGS=-g -Wall
LIBS=-lzmq

all:
	$(CC) $(CFLAGS) -o server server.cpp $(LIBS)
	$(CC) $(CFLAGS) -o client client.cpp $(LIBS)

clean:
	rm server client

