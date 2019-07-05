#include <stdio.h>

int main()
{
  int i, j;
  float x, y;
  char c;

  printf("\n====== INPUT ======\n");
  scanf("%d  %d   %f  \n  \n %f", &i, &j, &x, &y);
  printf("\n====== PRINT ======\n");
  printf("%d\n%d\n%f\n%f\n", i, j, x, y);
  /* 1.
  As it searches for the beginning of a number, scanf ignores white-space characters (the space, horizontal and vertical tab, form-feed, and new-line characters).

  As a result, numbers can be put on a single line or spread out over several lines.
 */

  // ====== INPUT ======
  //   1
  // -20   .3
  //
  //   -4.0e3
  //
  // ====== PRINT ======
  // 1
  // -20
  // 0.300000
  // -4000.000000

  printf("\n====== INPUT ======\n");

  scanf("  %d  \n   \n   \n", &i);
  scanf("%c", &c);
  printf("\n====== PRINT ======\n");
  printf("%d, %c", i, c);
  // ====== INPUT ======
  // 222
  //
  //
  // y
  //
  // ====== PRINT ======
  // 222, y

  /* 2.
  When scanf encounters a character that can't be part of the current item, the caracter is "put back" to be read again during the scanning of the next input item or during the next call of scanf.
 */

  /* 3.
  If the format string is " %d\n", scanf will skip white space, read an integer, then skip to the next non-white-space character. A format string like this can cause an interactive program to "hang" until the user enters a nonblank character.
  (" " is equally treated as a "\n" in the format string of scanf as they are all white-space characters.)
 */

  return 0;
}
