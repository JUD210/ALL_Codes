/* Write calls of printf that display a float variable x in the following formats. 

(a) Exponential notation; left-justified in a field of size 8; one digit after the decimal point.
(b) Exponential notation; right-justified in a field of size 10; six digits after the decimal point.
(c) Fixed decimal notation; left-justified in a field of size 8; three digits after the decimal point.
(d) Fixed decimal notation; right-justified in a field of size 6; no digits after the decimal point.

*/

#include <stdio.h>

int main()
{
  float x;
  x = 123456.654321f;

  printf("%-8.1e\n", x);
  printf("%10.6e\n", x);
  printf("%-8.3f\n", x);
  printf("%6.0f\n", x);
  // 1.2e+005
  // 1.234567e+005
  // 123456.656
  // 123456.656250

  return 0;
}
