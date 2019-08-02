//In this challenge, write a program that takes in three arguments, a start temperature (in Celsius),
//an end temperature (in Celsius) and a step size. Print out a table that goes from the start
//temperature to the end temperature, in steps of the step size; you do not actually need to print the
//final end temperature if the step size does not exactly match. You should perform input validation:
//do not accept start temperatures less than a lower limit (which your code should specify as a constant)
//or higher than an upper limit (which your code should also specify). You should not allow a step size
//greater than the difference in temperatures. (This exercise was based on a problem from C Programming
//Language).

#include <iostream>
#include <assert.h>

double convertTemperature(double degreesCelsius){
    double degreesFarenheit;
    degreesFarenheit = (degreesCelsius * 9/5) + 32;
    return degreesFarenheit;
}

int main(int argc, char *argv[]){

    double minTemperatureCelsius;
    minTemperatureCelsius = atof(argv[1]);
    double maxTemperatureCelsius;
    maxTemperatureCelsius = atof(argv[2]);
    double stepSize;
    stepSize = atof(argv[3]);

    assert(minTemperatureCelsius > -50.0);
    assert(maxTemperatureCelsius < 500.0);
    assert(stepSize > 0.0);
    std::cout << convertTemperature(0) << std::endl;
    std::cout << convertTemperature(100) << std::endl;
    std::cout << convertTemperature(50) << std::endl;

    unsigned elements = (maxTemperatureCelsius - minTemperatureCelsius) / stepSize;

    double temp = minTemperatureCelsius;
    for(auto i = 0; i < elements; i++){
        std::cout << "Celsius: " << temp << " Farenheit: " << convertTemperature(temp) << std::endl;
        temp += stepSize;
    }
}

