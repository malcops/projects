#include <assert.h>
#include <iostream>
#include <fstream>
#include <map>


double calculateGCContent(std::string dnaString){
    int countGC = 0;
    int total = dnaString.length();
    for(auto it=dnaString.begin(); it!=dnaString.end(); ++it){
        if(*it == 'G' | *it == 'C'){
            countGC += 1;
        }
    }
    std::cout << "GC " << countGC << std::endl;
    std::cout << "total " << total << std::endl;

    assert(total != 0);
    double percentage = countGC/(double)total*100;
    // std::cout << "percentage " << percentage << std::endl;
    return percentage;
}


int main(void){

    std::ifstream input("rosalind_gc.txt");
    std::string line;
    std::map<std::string, std::string> dnaStrings;

    std::string id;
    std::string sequence;

    while(std::getline(input, line)){
        if(line.at(0) == '>'){
            if(sequence.length()){
                dnaStrings[id] = sequence;
            }
            sequence = "";
            id = line.substr(1,line.npos);
        }
        else{
            sequence += line;
        }
    }
    dnaStrings[id] = sequence;
    input.close();

    std::string highestId = "";
    double highestPercentage = 0.0;
    for(auto it=dnaStrings.begin(); it!=dnaStrings.end(); ++it){
        // std::cout << it->first << " " << it->second << std::endl;
        double thisPercentage = calculateGCContent(it->second);
        if(thisPercentage > highestPercentage){
            highestId=it->first;
            highestPercentage = thisPercentage;
        };
    }
    std::cout << "Final answer:" << std::endl;
    std::cout << highestId << std::endl;
    std::cout.unsetf(std::ios::floatfield);
    std::cout.precision(9);
    std::cout << highestPercentage << std::endl;

    return 0;
}
