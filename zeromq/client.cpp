#include <zmq.hpp>
#include <string>
#include <iostream>
#include <unistd.h>

using namespace std;

void show_info() {
    int major, minor, patch;
    zmq_version(&major, &minor, &patch);
    printf("Using 0MQ version %02d.%d.%d\n", major, minor, patch);
}

int main(int argc, char** argv)
{
    show_info();
    zmq::context_t context(1);
    zmq::socket_t subscriber(context, ZMQ_SUB);


    //open socket to server to get updates
    cout << "Collecting updates from server\n";
    subscriber.connect("tcp://192.168.7.2:5555");

    // subscribe to all?
	subscriber.setsockopt(ZMQ_SUBSCRIBE, "", 0);
    while(1){
        zmq::message_t msg;
        subscriber.recv(&msg);

        string output = string(static_cast<char*>(msg.data()), msg.size());

        cout << output << endl;
    }

    //close 0MQ
	  subscriber.close();
  	context.close();
    system("PAUSE");
    return 0;
}
