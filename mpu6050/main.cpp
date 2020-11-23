#include "IMU.hpp"

int main(void){

    init();
    while(1){
        MPU6050 imu;
        auto accels = imu.readAccelXYZ(); 
        char accelOutput[128];
        snprintf(accelOutput, sizeof(accelOutput), "accels %f %f %f\n", accels.accel_X, accels.accel_Y, accels.accel_Z);
        std::cout << accelOutput << std::endl;

        auto gyros = imu.readGyroXYZ();
        char gyroOutput[50];
        snprintf(gyroOutput, sizeof(gyroOutput), "gyros %f %f %f\n", gyros.gyro_X, gyros.gyro_Y, gyros.gyro_Z);
        std::cout << gyroOutput << std::endl;

        std::cout << imu.readTemp() << std::endl;
        sleep(1);
    }

    return 0;
}
