/* Is the following if statement legal?

if (n == 1-10)
  printf(“n is between 1 and 10\n");

If so, what does it do when n is equal to 5? */

#include <stdio.h>

int main()
{
  for (int n = -10; n < 2; n++)
    if (n == 1 - 10)
      printf("[n:%d] n is between 1 and 10\n", n);
    else
      printf("[n:%d] n is NOT between 1 and 10\n", n);
  // [n:-10] n is NOT between 1 and 10
  // [n:-9] n is between 1 and 10
  // [n:-8] n is NOT between 1 and 10
  // [n:-7] n is NOT between 1 and 10
  // [n:-6] n is NOT between 1 and 10
  // [n:-5] n is NOT between 1 and 10
  // [n:-4] n is NOT between 1 and 10
  // [n:-3] n is NOT between 1 and 10
  // [n:-2] n is NOT between 1 and 10
  // [n:-1] n is NOT between 1 and 10
  // [n:0] n is NOT between 1 and 10
  // [n:1] n is NOT between 1 and 10

  return 0;
}

/*
  It is a legal statement.
  (Although it's not gonna work as we expect.)

  First, in the if's expression, 1 - 10 is evaluated to -9.
  Then, (n == -9) is evaluated as 0, meaning the final value is 0.
  Since the value is 0, it skips the printf statement and exits.

  Note: The precedence of equality operators is less than arithmetic operators.
 */