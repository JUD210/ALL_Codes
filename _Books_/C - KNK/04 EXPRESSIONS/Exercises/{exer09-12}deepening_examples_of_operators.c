/* exer 9-12

Show the output produced by each of the following program fragments. Assume that i, j, and k are int variables.

 */

#include <stdio.h>

int main() {
    int i, j, k;

    i = 7, j = 8;
    i *= j + 1;
    printf("%d %d\n", i, j);
    // 63 8

    i = j = k = 1;
    i += j += k;
    printf("%d %d %d\n", i, j, k);
    // 3 2 1

    i = 1, j = 2, k = 3;
    i -= j -= k;
    printf("%d %d %d\n", i, j, k);
    // 2 -1 3

    i = 2, j = 1, k = 0;
    i *= j *= k;
    printf("%d %d %d\n", i, j, k);
    // 0 0 0

    ////////////////////////////////////////////////////////////

    i = 6;
    j = i += i;
    printf("%d %d\n", i, j);
    // 12 12

    i = 5;
    j = (i -= 2) + 1;
    printf("%d %d\n", i, j);
    // 3 4

    i = 7;
    j = 6 + (i = 2.5);
    printf("%d %d\n", i, j);
    // 2 8

    i = 2, j = 8;
    j = (i = 6) + (j = 3);
    printf("%d %d\n", i, j);
    // 6 9

    ////////////////////////////////////////////////////////////

    i = 1;
    printf("%d ", i++ - 1);
    printf("%d\n", i);
    // 0 2
    i = 10, j = 5;
    printf("%d ", i++ - ++j);
    printf("%d %d\n", i, j);
    // 4 11 6

    i = 7, j = 8;
    printf("%d ", i++ - --j);
    printf("%d %d\n", i, j);
    // 0 8 7

    i = 3, j = 4, k = 5;
    printf("%d ", i++ - j++ + --k);
    printf("%d %d %d\n", i, j, k);
    // 3 4 5 4

    ////////////////////////////////////////////////////////////

    i = 5;
    j = ++i * 3 - 2;
    printf("%d %d\n", i, j);
    // 6 16

    i = 5;
    j = 3 - 2 * i++;
    printf("%d %d\n", i, j);
    // 6 -7

    i = 7;
    j = 3 * i-- + 2;
    printf("%d %d\n", i, j);
    // 6 23

    i = 7;
    j = 3 + --i * 2;
    printf("%d %d\n", i, j);
    // 6 15

    return 0;
}