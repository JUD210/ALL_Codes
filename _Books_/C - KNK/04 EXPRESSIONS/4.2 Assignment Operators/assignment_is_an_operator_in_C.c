#include <stdio.h>

int main()
{
  int i, j, k;
  i = j = k = 3;
  // i = (j = (k = 3));
  // The = operator is right associative.

  printf("%d\n", i = 5);
  printf("%d\n", j);
  printf("%d\n", k);
  // 5
  // 3
  // 3

  /*
  Watch out for unexpected results in chained assignments as a result of type conversion:
  */

  int x;
  float f;
  f = x = 33.3f;

  printf("%d\n", x);
  printf("%f\n", f);
  // 33
  // 33.000000

  return 0;
}