#include "gopro.hpp"
#include "HTTPRequest.hpp"
#include "json.hpp"

GoPro::GoPro(){}

int GoPro::keepOn(){
    std::string keepOn = "http://10.5.5.9/gp/gpControl/setting/59/0";
    HTTPRequest request1(keepOn);
    std::cout << request1.execute() << std::endl;
    return 0;
}

int GoPro::takePhoto(){
    std::string photoMode = "http://10.5.5.9/gp/gpControl/command/mode?p=1";
    HTTPRequest request1(photoMode);
    request1.execute();

    std::string start = "http://10.5.5.9/gp/gpControl/command/shutter?p=1";
    HTTPRequest request2(start);
    request2.execute();
    return 0;
}

int GoPro::startVideo(){

    std::string videoMode = "http://10.5.5.9/gp/gpControl/command/mode?p=0";
    HTTPRequest request1(videoMode);
    request1.execute();

    std::string start = "http://10.5.5.9/gp/gpControl/command/shutter?p=1";
    HTTPRequest request2(start);
    request2.execute();

    return 0;
}

int GoPro::stopVideo(){

    std::string stop = "http://10.5.5.9/gp/gpControl/command/shutter?p=0";
    HTTPRequest request(stop);
    request.execute();

    return 0;
}

int GoPro::locateOn(){

    std::string locate = "http://10.5.5.9/gp/gpControl/command/system/locate?p=1";
    HTTPRequest request(locate);
    request.execute();

    return 0;
}

int GoPro::locateOff(){

    std::string locate = "http://10.5.5.9/gp/gpControl/command/system/locate?p=0";
    HTTPRequest request(locate);
    request.execute();

    return 0;
}

std::string GoPro::getStatus(){
    std::string status = "http://10.5.5.9/gp/gpControl/status";
    HTTPRequest request(status);
    std::string response = request.execute();
    this->m_currentStatus = response;
    return response;
}

std::string GoPro::cameraName(){
    auto j = nlohmann::json::parse(this->m_currentStatus.c_str());
    std::string name = j["status"]["30"];
    return name;
}

unsigned GoPro::getBatteryLevel(){
    // 4 = Charging
    // 3 = Full
    // 2 = Halfway
    // 1 = Low
    // 0 = Empty
    auto j = nlohmann::json::parse(this->m_currentStatus.c_str());
    unsigned batteryLevel = j["status"]["2"];
    return batteryLevel;
}

bool GoPro::sdCardInserted(){
    // 0 - inserted
    // 2 - not found
    auto j = nlohmann::json::parse(this->m_currentStatus.c_str());
    unsigned inserted = j["status"]["33"];
    bool sdCardInserted = not static_cast<bool>(inserted);
    return sdCardInserted;
}

unsigned GoPro::getMode(){
    // Video - 0
    // Photo - 1
    // MultiShot - 2
    auto j = nlohmann::json::parse(this->m_currentStatus.c_str());
    unsigned currentMode = j["status"]["43"];
    return currentMode;
}

unsigned GoPro::getSubMode(){
    // 0 = Video/Single Pic/Burst
    // 1 = TL Video/Continuous/TimeLapse
    // 2 = Video+Photo/NightPhoto/NightLapse
    auto j = nlohmann::json::parse(this->m_currentStatus.c_str());
    unsigned subMode = j["status"]["44"];
    return subMode;
}

unsigned GoPro::getSpaceRemaining(){
    // remaining space in bytes
    auto j = nlohmann::json::parse(this->m_currentStatus.c_str());
    unsigned spaceRemaining = j["status"]["54"];
    return spaceRemaining;
}

unsigned GoPro::getOrientation(){
    // Auto - 0
    // UP - 1
    // DOWN - 2
    auto j = nlohmann::json::parse(this->m_currentStatus.c_str());
    unsigned orientation = j["settings"]["52"];
    return orientation;
}
