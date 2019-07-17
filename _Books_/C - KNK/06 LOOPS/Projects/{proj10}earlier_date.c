/* Programming Project 9 in Chapter 5 asked you to write a program that determines which of two dates comes earlier on the calendar. Generalize the program so that the user may enter any number of dates. The user will enter 0/0/0 to indicate that no more dates will be entered:

Enter a date (mm/dd/yy) : 3/6/08
Enter a date (mm/dd/yy) : 5/17/07
Enter a date (mm/dd/yy) : 6/3/07
Enter a date (mm/dd/yy) : O/O/O
5/17/07 is the earliest date
 */

#include <stdio.h>

int main() {
    int month, day, year,
        month_earliest, day_earliest, year_earliest,
        is_earliest;

    month_earliest = 12;
    day_earliest = 31;
    year_earliest = 99;
    for (;;) {
        printf("Enter a date (mm/dd/yy): ");
        scanf("%d/%d/%d", &month, &day, &year);

        /* Exit the loop */
        if (month == 0 || day == 0)
            break;

        /* determine if this date is the earliest date. */
        if (year < year_earliest)
            is_earliest = 1;
        else if (year > year_earliest)
            is_earliest = 0;
        else if (month < month_earliest)
            is_earliest = 1;
        else if (month > month_earliest)
            is_earliest = 0;
        else if (day < day_earliest)
            is_earliest = 1;
        else if (day > day_earliest)
            is_earliest = 0;

        if (is_earliest) {
            month_earliest = month;
            day_earliest = day;
            year_earliest = year;
        }
    }

    printf("%d/%d/%.2d is the earliest date",
           month_earliest, day_earliest, year_earliest);

    // Enter a date (mm/dd/yy) : 3/6/08
    // Enter a date (mm/dd/yy) : 5/17/07
    // Enter a date (mm/dd/yy) : 6/3/07
    // Enter a date (mm/dd/yy) : O/O/O
    // 5/17/07 is the earliest date

    return 0;
}