/* Write a program that asks the user for a 24-hour time. then displays the time in 12-hour form:

Enter a 24-hour time: 21:11 (input)
Equivalent 12-hour time: 9:11 PM

Be careful not to display 12:00 as 0:00. */

#include <stdio.h>

int main()
{
  int hours, minutes;

  printf("Enter a 24-hour time: ");
  scanf("%d:%d", &hours, &minutes);
  // Enter a 24-hour time: 12:00

  printf("Equivalent 12-hour time: ");
  if (hours == 0)
    printf("12:%.2d AM\n", minutes);
  else if (hours < 12)
    printf("%d:%.2d AM\n", hours, minutes);
  else if (hours == 12)
    printf("%d:%.2d PM\n", hours, minutes);
  else
    printf("%d:%.2d PM\n", hours - 12, minutes);
  // Equivalent 12-hour time: 12:00 PM

  return 0;
}
