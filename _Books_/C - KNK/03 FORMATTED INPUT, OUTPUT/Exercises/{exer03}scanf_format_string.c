/* For each of the following pairs of scanf format strings, indicate whether or not the two strings are equivalent. If they're not, show how they can be distinguished.

(a) "%d"        versus " %d"
(b) "%d-%d-%d"  versus "%d -%d -%d"
(c) "%f"        versus "%f "
(d) "%f,%f"     versus "%f, %f"

*/

#include <stdio.h>

int main() {
    int a, b, c;
    float x, y;

    ////////////////////////////
    printf("\n=== a ===\n");

    scanf("%d", &a);
    printf("|%d|\n", a);
    while (getchar() != '\n')
        ;
    // Used to clear buffers even if I type an improper character.

    printf("vs\n");

    scanf(" %d", &a);
    printf("|%d|\n", a);
    while (getchar() != '\n')
        ;

    /*

  === a ===
     12 34
  |12|
  vs
     12 34
  |12|

   */

    ////////////////////////////
    printf("\n=== b ===\n");

    scanf("%d-%d-%d", &a, &b, &c);
    printf("|%d|%d|%d|\n", a, b, c);
    while (getchar() != '\n')
        ;

    printf("vs\n");

    scanf("%d -%d -%d", &a, &b, &c);
    printf("|%d|%d|%d|\n", a, b, c);
    while (getchar() != '\n')
        ;

    /*

  === b ===
  1-2-3
  |1|2|3|
  vs
  1-2-3
  |1|2|3|

   */

    ////////////////////////////
    printf("\n=== c ===\n");

    scanf("%f", &x);
    printf("|%f|\n", x);
    while (getchar() != '\n')
        ;

    printf("vs\n");

    scanf("%f ", &x);
    printf("|%f|\n", x);
    while (getchar() != '\n')
        ;

    /*

  === c ===
  1.23
  |1.230000|
  vs
  1.23


  r
  |1.230000|

   */

    ////////////////////////////
    printf("\n=== d ===\n");

    scanf("%f,%f", &x, &y);
    printf("|%f|%f|\n", x, y);
    while (getchar() != '\n')
        ;

    printf("vs\n");

    scanf("%f, %f", &x, &y);
    printf("|%f|%f|\n", x, y);
    while (getchar() != '\n')
        ;

    /*

  === d ===
  1.23,4.56
  |1.230000|4.560000|
  vs
  1.23,4.56
  |1.230000|4.560000|

  */

    return 0;
}
