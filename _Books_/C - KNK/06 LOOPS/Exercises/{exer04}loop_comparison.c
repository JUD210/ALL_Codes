/* Which one of the following statements is not equivalent to the other two (assuming that the loop bodies are the same)?

(a) for (i = 0; i < 10; i++) ...
(b) for (i = 0; i < 10; ++i) ...
(c) for (i = 0; i++ < 10; ) ...
 */

#include <stdio.h>

int main()
{
  int i;

  for (i = 0; i < 10; i++)
    continue;
  printf("i: %d\n", i);
  // i: 10

  for (i = 0; i < 10; ++i)
    continue;
  printf("i: %d\n", i);
  // i: 10

  for (i = 0; i++ < 10;)
    continue;
  printf("i: %d\n", i);
  // i: 11

  return 0;
}