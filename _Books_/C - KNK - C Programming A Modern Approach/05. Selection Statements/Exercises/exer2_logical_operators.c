/* The following program fragments illustrate the logical operators. Show the output produced by each, assuming that i, j, and k are int variables. */

#include <stdio.h>

int main()
{
  int i, j, k;

  i = 10, j = 5;
  printf("%d\n", !i < j);
  // 1

  i = 2, j = 1;
  printf("%d\n", !!i + !j);
  // 1

  i = 5, j = 0, k = -5;
  printf("%d\n", i && j || k);
  // 1

  i = 1, j = 2, k = 3;
  printf("%d\n", i < j || k);
  // 1

  if (-5)
    printf("-5 is true");
  else
    printf("-5 is false");
  // -5 is true

  return 0;
}