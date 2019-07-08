//
//  Hello World server in C++
//  Binds PUB socket to tcp://*:5555
//
#include <zmq.hpp>
#include <string>
#include <sys/sysinfo.h>
#include <iostream>
#include <unistd.h>

void show_info() {
    int major, minor, patch;
    zmq_version(&major, &minor, &patch);
    printf("Using 0MQ version %02d.%d.%d\n", major, minor, patch);
}

int main () {

    show_info();
    //  Prepare our context and socket
    zmq::context_t context (1);
    zmq::socket_t publisher(context, ZMQ_PUB);
    publisher.bind ("tcp://*:5555");

    while (true) {

        //  Do some 'work'
        sleep(1);

	// get sysinfo
	struct sysinfo info;
	sysinfo(&info);

	std::string uptime = std::to_string(info.uptime);
	std::cout << uptime << std::endl;
        //  Publish msg to all subscribers on network
        const unsigned MSG_LENGTH=uptime.size();
        zmq::message_t msg_to_send(MSG_LENGTH);
    	memcpy (msg_to_send.data(), uptime.c_str(), MSG_LENGTH);
        //memcpy (msg_to_send.data (), "Hi There!", MSG_LENGTH);
        publisher.send (msg_to_send);
    }
    return 0;
}

