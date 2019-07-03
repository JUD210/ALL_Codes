/* Find the error in the following program fragment and f‌ix it.

if (n % 2 == 0);
  printf("n is even\n");
 */

#include <stdio.h>

int main()
{
  int n = 4;

  // if (n % 2 == 0);
  //   printf("n is even\n");

  if (n % 2 == 0)
    printf("n is even\n");
  // n is even

  return 0;
}