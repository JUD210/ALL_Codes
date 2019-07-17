/* Write a program that prompts the user to enter two dates and then indicates which date comes earlier on the calendar:

Enter first date (mm/dd/yy): 3/6/08 (input)
Enter second date (mm/dd/yy): 5/17/07 (input)

5/17/07 is earlier than 3/6/08 */

#include <stdio.h>

int main() {
    int month1, day1, year1,
        month2, day2, year2,
        is_former_earliest;

    printf("Enter first date (mm/dd/yy): ");
    scanf("%d/%d/%d", &month1, &day1, &year1);
    // Enter first date (mm/dd/yy): 3/6/08

    printf("Enter second date (mm/dd/yy): ");
    scanf("%d/%d/%d", &month2, &day2, &year2);
    // Enter second date (mm/dd/yy): 5/17/07

    /* determine which of two dates comes earlier. */
    if (year1 < year2)
        is_former_earliest = 1;
    else if (year1 > year2)
        is_former_earliest = 0;
    else if (month1 < month2)
        is_former_earliest = 1;
    else if (month1 > month2)
        is_former_earliest = 0;
    else if (day1 < day2)
        is_former_earliest = 1;
    else if (day1 > day2)
        is_former_earliest = 0;

    /* Result */
    if (is_former_earliest)
        printf("%d/%d/%.2d is earlier than %d/%d/%.2d",
               month1, day1, year1,
               month2, day2, year2);
    else
        printf("%d/%d/%.2d is earlier than %d/%d/%.2d",
               month2, day2, year2,
               month1, day1, year1);
    // 5/17/07 is earlier than 3/6/08

    return 0;
}