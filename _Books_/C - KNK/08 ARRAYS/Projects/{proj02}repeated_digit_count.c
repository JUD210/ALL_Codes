/* Modify the repdigit.c program of Section 8.1 so that it prints at table showing how many times each digit appears in the number:

Enter a number: 41271092 (input)
Digit:       0 1 2 3 4 5 6 7 8 9
Occurrences: 1 2 2 0 1 0 0 1 0 1
 */

#include <stdio.h>

int main() {
    int digit_count[10] = {0};

    int digit;
    long n;

    printf("Enter a number: ");
    scanf("%ld", &n);

    while (n > 0) {
        digit = n % 10;
        digit_count[digit]++;

        n /= 10;
    }

    printf("Digit:        0  1  2  3  4  5  6  7  8  9\n");
    printf("Occurrences:");
    for (int i = 0; i < 10; i++) {
        printf("%3d", digit_count[i]);
    }

    return 0;
}

// Enter a number: 41271092
// Digit:        0  1  2  3  4  5  6  7  8  9
// Occurrences:  1  2  2  0  1  0  0  1  0  1
