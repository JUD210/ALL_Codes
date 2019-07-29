/* Write a program that asks the user to enter a fraction, then reduces the fraction to lowest terms:

Enter a fraction: 6/12
In lowest terms: 1/2

Hint: To reduce a fraction to lowest terms, first compute the GCD of the numerator and denominator. Then divide both the numerator and denominator by the GCD. */

#include <stdio.h>

int main() {
    int numerator, denominator;

    printf("Enter a fraction: ");
    scanf("%d/%d", &numerator, &denominator);
    // Enter a fraction: 6/12

    int m, n, remainder, gcd;
    m = denominator;
    n = numerator;

    while (n != 0) {
        remainder = m % n;
        m = n;
        n = remainder;
    }
    gcd = m;

    printf("In lowest terms: %d/%d", numerator / gcd, denominator / gcd);
    // In lowest terms: 1/2

    return 0;
}