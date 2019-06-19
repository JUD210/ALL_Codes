/* Give the values of i and j after each of the following expression statements has been executed. (Assume that i has the value 1 initially and j has the value 2.)
 */

#include <stdio.h>

int main()
{

  int i, j;

  i = 1, j = 2;
  i += j;
  printf("i:%d, j:%d\n", i, j);
  // i:3, j:2

  i = 1, j = 2;
  i--;
  printf("i:%d, j:%d\n", i, j);
  // i:0, j:2

  i = 1, j = 2;
  i *j / i;
  printf("i:%d, j:%d\n", i, j);
  // i:1, j:2

  i = 1, j = 2;
  i % ++j;
  printf("i:%d, j:%d\n", i, j);
  // i:1, j:3

  return 0;
}
