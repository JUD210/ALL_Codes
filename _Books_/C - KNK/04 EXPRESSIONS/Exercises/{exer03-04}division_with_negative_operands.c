/* exer 3

What is the value of each of the following expressions in C89? (Give all possible values if an expression may have more than one value.)

(a) 8 / 5
(b) -8 / 5
(e) 8 / -5
(d) -8 / -5


////////////////////////////////////////////////////////////

   exer 4

Repeat Exercise 3 for C99.
 */

#include <stdio.h>
int main()
{
  // ONLY in C99

  printf("%d\n", 8 / 5);
  // 1
  printf("%d\n", -8 / 5);
  // -1
  printf("%d\n", 8 / -5);
  // -1
  printf("%d\n", -8 / -5);
  // 1

  return 0;
}