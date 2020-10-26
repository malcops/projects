#include <string>

class GoPro {

    public:
        GoPro();
        // commands
        int keepOn();
        int takePhoto();
        int startVideo();
        int stopVideo();
        int locateOn();
        int locateOff();
        
        // status
        std::string getStatus();
        std::string cameraName();
        unsigned getBatteryLevel();
        bool sdCardInserted();
        unsigned getMode();
        unsigned getSubMode();
        unsigned getSpaceRemaining();
        // settings
        unsigned getOrientation();
        std::string m_currentStatus;
};

