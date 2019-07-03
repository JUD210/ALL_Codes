/* Translate the program fragment of Exercise 2 into a single for statement.

#include <stdio.h>

int main()
{
  int i = 9384;
  do
  {
    printf("%d ", i);
    i /= 10;
  } while (i > 0);
  // 9384 938 93 9

  return 0;
}
*/

#include <stdio.h>

int main()
{
  for (int i = 9384; i > 0; i /= 10)
  {
    printf("%d ", i);
  }
  // 9384 938 93 9

  return 0;
}