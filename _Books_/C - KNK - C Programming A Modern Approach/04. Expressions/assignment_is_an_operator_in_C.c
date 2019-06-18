#include <stdio.h>

int main()
{
  /* 
  In many programming languages, assignment is a statement; in C, however, assignment is an operator, just like +. 
  
  In other words, the act of assignment produces a result, just as adding two numbers produces a result. The value of an assignment v = e is the value of v after the assignment. Thus, the value of i = 72.99f is 72 (not 72.99).
   */

  /* Side Ef‌lects
  We don't normally expect operators to modify their operands, since operators in mathematics don’t. Writing i + j doesn’t modify either i or j; it simply computes the result of adding 1 and j.

  Most C operators don't modify their operands, but some do. We say that these operators have side effects, since they do more than just compute a value. The simple assignment operator is the first operator we’ve seen that has side effects; it modifies its left operand. Evaluating the expression i = 0 produces the result 0 and — as a side effect — assigns 0 to i.
  */

  int i, j, k;
  i = j = k = 3;
  // i = (j = (k = 3));
  // The = operator is right associative.

  printf("%d\n", i = 5);
  printf("%d\n", j);
  printf("%d\n", k);
  // 5
  // 3
  // 3

  /* 
  Watch out for unexpected results in chained assignments as a result of type conversion: 
  */

  int x;
  float f;
  f = x = 33.3f;

  printf("%d\n", x);
  printf("%f\n", f);
  // 33
  // 33.000000

  return 0;
}