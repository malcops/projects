#include <sys/sysinfo.h>
#include <chrono>
#include <iostream>
#include <thread>

int main(void){
   
    struct sysinfo pcInfo;

    while(1){
        sysinfo(&pcInfo);   
        std::cout << "Uptime: " << pcInfo.uptime << std::endl;
        std::cout << "Total RAM (Gb): " << pcInfo.totalram / 1e9 << " Free RAM (Gb): " << pcInfo.freeram / 1e9 << "\n" << std::endl;

        std::this_thread::sleep_for(std::chrono::seconds(1));
    }




    return 0;

}


