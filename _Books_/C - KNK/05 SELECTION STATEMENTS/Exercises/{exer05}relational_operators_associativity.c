/* Is the following if statement legal?

if (n >= 1 <= 10)
  printf("n is between 1 and 10\n");

If so, what does it do when n is equal to 0? */

#include <stdio.h>

int main() {
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
  It is a legal statement.
  (Although it's not gonna work as we expect.)

  Here's what happens when n equals 0:

  First, in the if's expression, (n >= 1) is evaluated to 0.
  Then, (0 <= 10) is evaluated as 1, meaning the final value is 1.
  Since the value isn't 0, it runs the printf statement.

  Note: Comparison operations are left associative.
 */