/* What output do the following calls of printf produce? */

#include <stdio.h>

int main()
{
  printf("|%6.4d|%-5d|\n", 86, 1040);
  printf("|%15.5e|\n", 30.253);
  printf("|%.4f|\n", 83.162);
  printf("|%-8.2g|\n", .0000009979);
  // |  0086|1040 |
  // |   3.02530e+001|
  // |83.1620|
  // |1e-006  |

  return 0;
}
