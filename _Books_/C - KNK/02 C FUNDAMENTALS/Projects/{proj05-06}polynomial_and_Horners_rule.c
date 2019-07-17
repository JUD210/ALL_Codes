/* proj5

Write a program that asks the user to enter a value for x and then displays the value of the following polynomial:

3x^5 + 2x^4 - 5x^3 - x^2 + 7x - 6

Hint: C doesn't have an exponentiation operator, so you'll need to multiply x by itself repeatedly in order to compute the powers of x. (For example, x * x * x is x cubed.)

////////////////////////////////////////////////////////////

   proj6

Modify the program of Programming Project 5 so that the polynomial is evaluated using the following formula:

((((3x + 2)x - 5)x - 1)x + 7)x - 6

Note that the modified program performs fewer multiplications. This technique for evaluating polynomials is known as Horner's Rule.

 */

#include <stdio.h>

int main() {
    int x;
    printf("Enter the value of x: ");
    scanf("%d", &x);
    // Enter the value of x: 10

    int result_1, result_2;

    result_1 = 3 * x * x * x * x * x + 2 * x * x * x * x - 5 * x * x * x - x * x + 7 * x - 6;
    result_2 = ((((3 * x + 2) * x - 5) * x - 1) * x + 7) * x - 6;

    printf("Result 1. normal: %d\n", result_1);
    printf("Result 2. Horner's Rule: %d", result_2);
    // Result 1. normal: 314964
    // Result 2. Horner's Rule: 314964

    return 0;
}