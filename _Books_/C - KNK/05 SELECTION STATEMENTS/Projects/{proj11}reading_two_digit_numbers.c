/* Write a program that asks the user for a two-digit number. then prints the English word for the number:

Enter a two-digit number: 45 (input)
You entered the number forty-five.

Hint: Break the number into two digits. Use one switch statement to print the word for the f‌irst digit ("twenty-", "thirty-", and so forth). Use a second switch statement to print the word for the second digit. Don't forget that the numbers between 11 and 19 require special treatment. */

#include <stdio.h>

int main()
{
  int num;

  printf("Enter a two-digit number: ");
  scanf("%d", &num);

  printf("You entered the number ");

  switch (num / 10)
  {
  case 9:
    printf("ninety");
    break;
  case 8:
    printf("eighty");
    break;
  case 7:
    printf("seventy");
    break;
  case 6:
    printf("sixty");
    break;
  case 5:
    printf("fifty");
    break;
  case 4:
    printf("fourty");
    break;
  case 3:
    printf("thirty");
    break;
  case 2:
    printf("twenty");
    break;
  case 1:
    switch (num - (num / 10) * 10)
    {
    case 9:
      printf("nineteen");
      break;
    case 8:
      printf("eighteen");
      break;
    case 7:
      printf("seventeen");
      break;
    case 6:
      printf("sixteen");
      break;
    case 5:
      printf("fifteen");
      break;
    case 4:
      printf("fourteen");
      break;
    case 3:
      printf("thirteen");
      break;
    case 2:
      printf("twelve");
      break;
    case 1:
      printf("eleven");
      break;
    case 0:
      printf("ten");
      break;
    }
  }

  if (num / 10 != 1)
  {
    switch (num - (num / 10) * 10)
    {
    case 9:
      printf("-nine");
      break;
    case 8:
      printf("-eight");
      break;
    case 7:
      printf("-seven");
      break;
    case 6:
      printf("-six");
      break;
    case 5:
      printf("-five");
      break;
    case 4:
      printf("-four");
      break;
    case 3:
      printf("-three");
      break;
    case 2:
      printf("-two");
      break;
    case 1:
      printf("-one");
      break;
    }
  }

  printf(".");
  return 0;
}