/* Only one of the expressions ++i and i++ is exactly the same as (i += 1); which is it? Justify your answer.
*/

/* The expression ++i is equivalent to (i += 1). The value of both expressions is i after the increment has been performed.
 */

#include <stdio.h>

int main()
{
  int i;

  i = 5;
  printf("%d\n", ++i);
  // 6

  i = 5;
  printf("%d\n", i += 1);
  // 6

  i = 5;
  printf("%d\n", i++);
  // 5

  return 0;
}