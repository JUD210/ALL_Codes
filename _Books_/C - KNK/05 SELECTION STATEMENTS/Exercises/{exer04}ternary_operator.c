/* Write a single expression whose value is either -1, 0, or +1, depending on whether i is less than, equal to, or greater than j, respectively. */

#include <stdio.h>

int main() {
    int i, j;

    i = 1, j = 5;
    printf("%d\n", (i > j) - (i < j));
    // -1

    i = 5, j = 5;
    printf("%d\n", (i > j) - (i < j));
    // 0

    i = 9, j = 5;
    printf("%d\n", (i > j) - (i < j));
    // 1

    return 0;
}