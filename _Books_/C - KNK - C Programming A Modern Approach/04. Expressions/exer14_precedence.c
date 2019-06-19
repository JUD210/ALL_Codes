/* Supply parentheses to show how a C compiler would interpret each of the following expressions. */

#include <stdio.h>

int main()
{
  int a, b, c, d, e;
  a = 1, b = 20, c = 300, d = 4000, e = 50000;

  printf("%d\n", a * b - c * d + e);
  printf("%d\n", ((a * b) - (c * d)) + e);
  // -1149980

  printf("%d\n", a / b % c / d);
  printf("%d\n", ((a / b) % c) / d);
  // 0

  printf("%d\n", -a - b + c - +d);
  printf("%d\n", (-a) - b + c - (+d));
  // -3721

  printf("%d\n", a * -b / c - d);
  printf("%d\n", ((a * (-b)) / c) - d);
  // -4000

  return 0;
}