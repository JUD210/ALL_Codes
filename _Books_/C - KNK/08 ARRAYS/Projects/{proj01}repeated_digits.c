/* Modify the repdigit.c program of Section 8.1 so that it shows which digits (if any) were repeated:

Enter a number: 939577 (input)
Repeated digit(s): 7 9
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

    printf("Repeated digit(s): ");
    for (int i = 0; i < 10; i++) {
        if (digit_count[i] > 1) {
            printf("%d ", i);
        }
    }

    return 0;
}

// Enter a number: 939577
// Repeated digit(s): 7 9
