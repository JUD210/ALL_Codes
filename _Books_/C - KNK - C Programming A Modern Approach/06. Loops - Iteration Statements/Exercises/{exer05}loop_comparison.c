/* Which one of the following statements is not equivalent to the other two
(assuming that the loop bodies are the same)?

(a) while (i < 10) {...}
(b) for (; i < 10;) {...}
(c) do {...} while (i < 10);
 */

#include <stdio.h>

int main()
{
  int i;

  while (i < 10)
    i++;
  printf("i: %d\n", i);
  // i: 10

  for (; i < 10;)
    i++;
  printf("i: %d\n", i);
  // i: 10

  do
  {
    i++;
  } while (i < 10);
  printf("i: %d\n", i);
  // i: 11

  return 0;
}