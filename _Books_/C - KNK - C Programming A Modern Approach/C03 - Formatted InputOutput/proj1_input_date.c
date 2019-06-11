/* Write a program that accepts a date from the user in the form mm/dd/yyyy and then displays it in the form yyyymmdd:

Enter a date (mm/dd/yyyy) : 2/17/2011 (input)
You entered the date 20110217

 */

#include <stdio.h>

int main()
{
  int month, day, year;

  printf("Enter a date (mm/dd/yyyy): ");
  scanf("%d/%d/%d", &month, &day, &year);
  // Enter a date (mm/dd/yyyy): 2/17/2011

  printf("You entered the date %d%.2d%.2d\n", year, month, day);
  // You entered the date 20110217

  return 0;
}
