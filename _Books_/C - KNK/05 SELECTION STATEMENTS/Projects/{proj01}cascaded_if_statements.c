/* Write a program that calculates how many digits a number contains:

Enter a number: 374 (input)
The number 374 has 3 digits

You may assume that the number has no more than four digits.

Hint: Use if statements to test the number. For example, if the number is between 0 and 9, it has one digit. If the number is between 10 and 99, it has two digits. */

#include <stdio.h>

int main()
{
  int num, count_digit;

  printf("Enter a number: ");
  scanf("%d", &num);
  // Enter a number: 374

  if (num < 10)
    count_digit = 1;
  else if (num < 100)
    count_digit = 2;
  else if (num < 1000)
    count_digit = 3;
  else if (num < 10000)
    count_digit = 4;
  else if (num < 100000)
    count_digit = 5;
  else if (num < 1000000)
    count_digit = 6;
  else if (num < 10000000)
    count_digit = 7;
  else if (num < 100000000)
    count_digit = 8;
  else if (num < 1000000000)
    count_digit = 9;

  printf("The number %d has %d digits", num, count_digit);
  // The number 374 has 3 digits

  return 0;
}