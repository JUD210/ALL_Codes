/* Suppose that we call scanf as follows:

scanf("%d%f%d", &i, &x, &j);

If the user enters

10.3 5 6

what will be the values of i, x, and j after the call? (Assume that i and j are int variables and x is a float variable.)

 */

#include <stdio.h>

int main() {
    int i, j;
    float x;

    scanf("%d%f%d", &i, &x, &j);
    // 10.3 5 6

    printf("|%d|%f|%d|", i, x, j);
    // |10|0.300000|5|

    return 0;
}
