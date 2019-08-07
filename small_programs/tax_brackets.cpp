// TAX BRACKETS:
// Up to $30000       0.00%
//       $30000      10.00%
//      $100000      25.00%
//      $250000      47.50%

#include <iostream>
#include <assert.h>
#include <algorithm>

#define INCOME_MIN 0
#define INCOME_MAX 999999999

double taxOwedInBracket(double lowerLimit, double upperLimit, double income, double marginalRate){

    double amountAboveLowerLimit = std::max(income - lowerLimit, 0.0);
    double amountTaxed = std::min(amountAboveLowerLimit, upperLimit - lowerLimit);
    return amountTaxed * marginalRate;
}

int main(int argc, char *argv[]){

    assert(argv[1]);
    double annualIncome = atof(argv[1]);
    assert(annualIncome >=  INCOME_MIN);

    double tax = 0;
    tax = taxOwedInBracket(INCOME_MIN, 30000, annualIncome, 0.0)
        + taxOwedInBracket(30000, 100000, annualIncome, 0.1)
        + taxOwedInBracket(100000, 250000, annualIncome, 0.25)
        + taxOwedInBracket(250000, INCOME_MAX, annualIncome, 0.4750);

    std::cout << "Tax Owed: " << tax << std::endl;

    return 0;
}
