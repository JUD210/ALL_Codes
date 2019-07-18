/* Modify the sum.c program of Section 7.1 to sum a series of double values. */

#include <stdio.h>

int main() {
    double n;
    double sum = 0;

    printf("This program sums a series of doubles.\n");
    printf("Enter doubles (0 to terminate): ");
    scanf("%lf", &n);

    while (n != 0) {
        sum += n;
        scanf("%lf", &n);
    }

    printf("The sum is: %lf\n", sum);

    return 0;
}

// This program sums a series of doubles.
// Enter doubles (0 to terminate): 1
// 1.1
// 1.11
// 1.111
// 1.1111
// 0
// The sum is: 5.432100
