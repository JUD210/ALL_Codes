/* Rewrite the following loop so that its body is empty:

for (n = 0, m = 15; m > 0; n++)
  m /= 2;
 */

#include <stdio.h>

int main()
{
  int n, m;

  for (n = 0, m = 15; m > 0; n++)
    m /= 2;
  printf("n:%d, m:%d\n", n, m);
  // n:4, m:0

  for (n = 0, m = 15; m > 0; n++, m /= 2)
    ;
  // null statement
  // or continue;
  // or {}

  printf("n:%d, m:%d\n", n, m);
  // n:4, m:0

  return 0;
}