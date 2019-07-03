/* What output does the following program fragment produce? */

#include <stdio.h>

int main()
{
  int sum = 0;
  for (int i = 0; i < 10; i++)
  {
    if (i % 2)
      continue;
    sum += i;
  }
  printf("%d", sum);
  // 20  // 0 + 0+2+4+6+8

  return 0;
}
