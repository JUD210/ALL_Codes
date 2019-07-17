/* proj1

Write a program that asks the user to enter a two-digit number, then prints the number with its digits reversed. A session with the program should have the following appearance:

Enter a two-digit: number: 28 (input)
The reversal is: 82

Read the number using %d, then break it into two digits.

Hint: If n is an integer, then n % 10 is the last digit in n and n / 10 is n with the last digit removed.

////////////////////////////////////////////////////////////

   proj2

Extend the program in Programming Project 1 to handle three-digit numbers.

////////////////////////////////////////////////////////////

   proj 3

Rewrite the program in Programming Project 2 so that it prints the reversal of a three-digit number without using arithmetic to split the number into digits.

Hint: See the upc.c program of Section 4.1.

*/

#include <stdio.h>

int main() {
    int num2;

    printf("Enter a two-digit: number: ");
    scanf("%d", &num2);
    // Enter a two-digit: number: 28

    printf("The reversal is: %d%d\n", num2 % 10, num2 / 10);
    // The reversal is: 82

    ////////////////////////////////////////////////////////////

    int num3;
    printf("Enter a three-digit number: ");
    scanf("%d", &num3);
    // Enter a three-digit number: 159

    printf("The reversal is: %d%d%d\n", num3 % 10, (num3 / 10) % 10, num3 / 100);
    // The reversal is: 951

    ////////////////////////////////////////////////////////////

    int n1, n2, n3;
    printf("Enter a three-digit number: ");
    scanf("%1d%1d%1d", &n1, &n2, &n3);
    // Enter a three-digit number: 159

    printf("The reversal is: %1d%1d%1d\n", n3, n2, n1);
    // The reversal is: 951

    return 0;
}