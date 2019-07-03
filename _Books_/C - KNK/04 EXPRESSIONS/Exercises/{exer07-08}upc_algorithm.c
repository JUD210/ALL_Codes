/* exer 7

The algorithm for computing the UPC check digit ends with the following steps:

Subtract 1 from the total.
Compute the remainder when the adjusted total is divided by 10.
Subtract the remainder from 9.

It's tempting to try to simplify the algorithm by using these steps instead:

Compute the remainder when the total is divided by 10.
Subtract the remainder from l0.

Why doesn't this technique work?
 */

/* Then, Let's take a look at a counterexample.
When the value of 'total' is a multiple of 10 (10, 20, 30, ...)

In the former algorithm, ((total-1) % 10) results 9 always.
9 - ((total - 1) % 10)
= 9 - 9
= 0

In the latter algorithm, (total % 10) results 0 always.
10 - (total % 10)
= 10 - 0
= 10

 */

////////////////////////////////////////////////////////////

/* exer 8

Would the upc.c program still work if the expression

9 - ((total - 1) % 10)
were replaced by

(10 - (total % 10)) % 10
?
 */

/* I guess if the value of total is greater than 0, It would be work. */

#include <stdio.h>

int main()
{
  int total;

  total = 100;
  printf("(Former) Check digit: %d\n", 9 - ((total - 1) % 10));
  printf("(Latter) Check digit: %d\n", 10 - (total % 10));
  printf("(Another) Check digit: %d\n", (10 - (total % 10)) % 10);
  // (Former) Check digit: 0
  // (Latter) Check digit: 10
  // (Another) Check digit: 0
  total = 0;
  printf("(Former) Check digit: %d\n", 9 - ((total - 1) % 10));
  printf("(Latter) Check digit: %d\n", 10 - (total % 10));
  printf("(Another) Check digit: %d\n", (10 - (total % 10)) % 10);
  // (Former) Check digit: 10
  // (Latter) Check digit: 10
  // (Another) Check digit: 0
  total = 5;
  printf("(Former) Check digit: %d\n", 9 - ((total - 1) % 10));
  printf("(Latter) Check digit: %d\n", 10 - (total % 10));
  printf("(Another) Check digit: %d\n", (10 - (total % 10)) % 10);
  // (Former) Check digit: 5
  // (Latter) Check digit: 5
  // (Another) Check digit: 5
  total = 36;
  printf("(Former) Check digit: %d\n", 9 - ((total - 1) % 10));
  printf("(Latter) Check digit: %d\n", 10 - (total % 10));
  printf("(Another) Check digit: %d\n", (10 - (total % 10)) % 10);
  // (Former) Check digit: 4
  // (Latter) Check digit: 4
  // (Another) Check digit: 4
  total = -36;
  printf("(Former) Check digit: %d\n", 9 - ((total - 1) % 10));
  printf("(Latter) Check digit: %d\n", 10 - (total % 10));
  printf("(Another) Check digit: %d\n", (10 - (total % 10)) % 10);
  // (Former) Check digit: 16
  // (Latter) Check digit: 16
  // (Another) Check digit: 6

  return 0;
}
