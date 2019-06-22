#include <stdio.h>

int main()
{
  float f;
  double d;

  /* Because by unsuffixed floating-point literals are doubles, and rounding means that even small literals can take on different values when rounded to float and double. 

  This can be observed in the following example:
   */

  f = 0.67;
  if (f == 0.67)
    printf("yes\n");
  else
    printf("no\n");
  // no

  /* This will output no, because 0.67 has a different value when rounded to float than it does when rounded to double. 

  On the other hand:
   */

  f = 0.67;
  if (f == 0.67f)
    printf("yes\n");
  else
    printf("no\n");
  // yes

  /*  this outputs yes.

  The suffix can be specified using either upper or lowercase letters.
  
  Try this also:
   */

  printf("%dbit vs %dbit\n", sizeof(.67f), sizeof(.67));
  // 4bit vs 8bit

  d = 0.67;
  if (d == 0.67)
    printf("yes\n");
  else
    printf("no\n");
  // yes

  d = 0.67;
  if (d == 0.67f)
    printf("yes\n");
  else
    printf("no\n");
  // no

  return 0;
}