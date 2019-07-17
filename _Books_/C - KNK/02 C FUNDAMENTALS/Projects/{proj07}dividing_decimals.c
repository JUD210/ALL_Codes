/* Write a program that asks the user to enter a U.S. dollar amount and then shows how to pay that amount using the smallest number of $20, $10, $5, and $1 bills:

Enter a dollar amount: 93 (input)

$20 bills: 4
$10 bills: 1
 $5 bills: 0
 $1 bills: 3

Hint: Divide the amount by 20 to determine the number of $20 bills needed, and then reduce the amount by the total value of the $20 bills. Repeat for the other bill sizes. Be sure to use integer values throughout, not floating-point numbers.

 */

#include <stdio.h>

int main() {
    int dollar;

    printf("Enter a dollar amount: ");
    scanf("%d", &dollar);
    // Enter a dollar amount: 93

    printf("$20 bills: %d\n", dollar / 20);
    // $20 bills: 4

    dollar -= 20 * (dollar / 20);
    printf("$10 bills: %d\n", dollar / 10);
    // $10 bills: 1

    dollar -= 10 * (dollar / 10);
    printf(" $5 bills: %d\n", dollar / 5);
    //  $5 bills: 0

    dollar -= 5 * (dollar / 5);
    printf(" $1 bills: %d", dollar / 1);
    //  $1 bills: 3

    return 0;
}
