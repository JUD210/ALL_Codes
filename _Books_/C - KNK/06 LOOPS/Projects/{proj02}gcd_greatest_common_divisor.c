/* Write a program that asks the user to enter two integers, then calculates and displays their greatest common divisor (GCD):

Enter two integers: 12 28 (input)
Greatest common divisor: 4

Hint: The classic algorithm for computing the GCD, known as Euclid's algorithm, goes as follows:

- Let m and n be variables containing the two numbers.
- if n is 0, then stop: in contains the GCD.
- Otherwise, compute the remainder when m is divided by n.
- Copy n into m and copy the remainder into n.
- Then repeat the process, starting with testing whether n is O.
 */

#include <stdio.h>

int main() {
    int m, n, remainder;

    printf("Enter two integers: ");
    scanf("%d%d", &m, &n);
    // Enter two integers: 12 28

    while (n != 0) {
        remainder = m % n;
        m = n;
        n = remainder;
    }

    printf("Greatest common divisor: %d\n", m);
    // Greatest common divisor: 4

    return 0;
}