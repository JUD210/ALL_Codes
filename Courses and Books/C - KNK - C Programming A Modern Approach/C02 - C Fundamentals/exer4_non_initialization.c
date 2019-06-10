/* Write a program that declares several int and float variables - without initializing them - and then prints their values. Is there any pattern to the values? (Usually there isn't.) */


#include <stdio.h>

int main()
{
  int i, j, k;
  float x, y, z;

  printf("Value of i: %d\n", i); // Value of i: 0
  printf("Value of j: %d\n", j); // Value of j: 16
  printf("Value of k: %d\n", k); // Value of k: 0
  printf("Value of x: %g\n", x); // Value of x: 2.8541e-039
  printf("Value of y: %g\n", y); // Value of y: 0
  printf("Value of z: %g\n", z); // Value of z: 1.75162e-043

  return 0;
}