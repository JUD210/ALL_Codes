/* Using the switch statement, write a program that converts a numerical grade into a letter grade:

Enter numerical grade: 84 (input)
Letter grade: B

Use the following grading scale:

A = 90—100, B = 80—89, C = 70~79, D = 60-69, F = 0-59.

Print an error message if the grade is larger than 100 or less than 0.

Hint: Break the grade into two digits, then use a switch statement to test the ten’s digit. */

#include <stdio.h>

int main()
{
  int grade;

  printf("Enter numerical grade: ");
  scanf("%d", &grade);

  if (grade < 0 || grade > 100)
  {
    printf("Illegal grade\n");
    return 0;
  }

  switch (grade / 10)
  {
  case 10:
  case 9:
    printf("Letter grade: A\n");
    break;
  case 8:
    printf("Letter grade: B\n");
    break;
  case 7:
    printf("Letter grade: C\n");
    break;
  case 6:
    printf("Letter grade: D\n");
    break;
  default:
    printf("Letter grade: F\n");
    break;
  }

  return 0;
}