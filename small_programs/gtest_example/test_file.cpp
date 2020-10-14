#include "source_file.hpp"
#include "gtest/gtest.h"

TEST(CalcTest, HandlesZeroInput) {
  EXPECT_EQ(calc(0), 0);
}

TEST(CalcTest, BasicCalc) {
  EXPECT_EQ(calc(16), 1.0);
}

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
