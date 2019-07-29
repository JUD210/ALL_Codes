/* Write a program that asks the user for a 12-hour time, than displays the time in 24-hour form:

Enter a 12-hour time: 9:11 PM (input)
Equivalent 24-hour time: 21:11

See Programming Project 8 for a description of the input format.
 */

#include <ctype.h>
#include <stdio.h>

int main() {
    int hour, minute, offset;
    char meridiem;

    printf("Please enter a time(hh:mm am/pm): ");
    scanf("%d:%d %c", &hour, &minute, &meridiem);

    offset = (toupper(meridiem) == 'P' ? 12 : 0);
    hour = (hour == 12 ? 0 : hour);
    // meridiem = toupper(meridiem);
    // if (meridiem == 'P') {
    //     if (hour != 12) {
    //         hour += 12;
    //     }
    // } else if (meridiem == 'A') {
    //     if (hour == 12) {
    //         hour -= 12;
    //     }
    // }

    printf("%.2d:%.2d", hour + offset, minute);

    return 0;
}

// Enter a 12-hour time: 9:11 PM
// Equivalent 24-hour time: 21:11
