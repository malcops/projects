#include <assert.h>
#include <iostream>
#include <fstream>
#include <string>


long int calculateRabbits(int n, int k){

    long int babyRabbits  = 1;
    long int adultRabbits = 0;
    long int totalRabbits = babyRabbits + adultRabbits;
    int month = 1;

    long int prevAdultRabbits = adultRabbits;
    adultRabbits += babyRabbits;
    babyRabbits = prevAdultRabbits*k;
    totalRabbits = babyRabbits + adultRabbits;
    month++;

    for(auto x=month; x<n; x++){
        prevAdultRabbits = adultRabbits;
        adultRabbits += babyRabbits;
        babyRabbits = prevAdultRabbits*k;
        totalRabbits = babyRabbits + adultRabbits;
        month++;
        // std::cout << "month " << month << std::endl;
        // std::cout << "adult " << adultRabbits << std::endl;
        // std::cout << "baby " << babyRabbits << std::endl;
        // std::cout << "total " << totalRabbits << std::endl;
    }
    return totalRabbits;
}


int main(void){

    std::ifstream input("rosalind_fib.txt");
    std::string inputString;
    std::getline(input, inputString,' ');
    int n = std::stoi(inputString);
    std::getline(input, inputString);
    int k = std::stoi(inputString);
    assert(n<=40);
    assert(k<=5);

    std::cout << "Final answer:" << std::endl;
    std::cout << calculateRabbits(n,k) << std::endl;
    return 0;
}
