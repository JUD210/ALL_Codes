/* Is the following if statement legal?

if (n >= 1 <= 10)
  printf(“n is between 1 and 10\n");

If so, what does it do when n is equal to 0? */

#include <stdio.h>

int main()
{
  for (int n = -2; n < 12; n++)
    if (n >= 1 <= 10)
      printf("[n:%d] n is between 1 and 10\n", n);
    else
      printf("[n:%d] n is NOT between 1 and 10\n", n);
  // [n:-2] n is between 1 and 10
  // [n:-1] n is between 1 and 10
  // [n:0] n is between 1 and 10
  // [n:1] n is between 1 and 10
  // [n:2] n is between 1 and 10
  // [n:3] n is between 1 and 10
  // [n:4] n is between 1 and 10
  // [n:5] n is between 1 and 10
  // [n:6] n is between 1 and 10
  // [n:7] n is between 1 and 10
  // [n:8] n is between 1 and 10
  // [n:9] n is between 1 and 10
  // [n:10] n is between 1 and 10
  // [n:11] n is between 1 and 10

  return 0;
}

/* 
  It is illegal. 
  
  As comparison operations are left associative, n is compared with 1, and then the result is compared with 10.

  n >= 1 yields 0 or 1, and then the 0 <= 10 or 1 <= 10 always yields 1 (true).

  In short, whatever n's value is, as the if's conditional expression always yields 1 (true), printf function would always be called.
 */