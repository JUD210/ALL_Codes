/* Programming Project 1 in Chapter 4 asked you to write a program that displays a two-digit number with its digits reversed. Generalize the program so that the number can have one, two, three, or more digits. Hint: Use a do loop that repeatedly divides the number by 10, stopping when it reaches 0. */

#include <stdio.h>

int main()
{
  int num;

  printf("Enter a number: ");
  scanf("%d", &num);
  // Enter a number: 281234

  printf("The reversal is: ");
  do
  {
    printf("%d", num % 10);
    num /= 10;
  } while (num != 0);
  // The reversal is: 432182

  return 0;
}