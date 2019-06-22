#include <stdio.h>
int main()
{
  int i;

  i = 1;
  printf("%d\n", ++i);
  printf("%d\n", i);
  // 2
  // 2

  /* Evaluating the expression i++ (a “post-increment") produces the result i, but causes i to be incremented afterwards.
   */

  i = 1;
  printf("%d\n", i++);
  printf("%d\n", i);
  // 1
  // 2

  int j, k;

  i = 1;
  j = 2;

  k = ++i + j++;
  // is equal to
  //
  // i = i + 1;
  // k = i + j;
  // j = j + 1;
  printf("i:%d | j:%d | k:%d\n", i, j, k);
  // i:2 | j:3 | k:4

  return 0;
}

/* For the record, the postf‌ix versions of ++ and -- have higher precedence than unary plus and minus and are left associative.

The pref‌ix versions have the same precedence as unary plus and minus and are right associative.
 */