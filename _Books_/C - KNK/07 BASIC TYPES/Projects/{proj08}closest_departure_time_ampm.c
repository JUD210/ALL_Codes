/* Modify Programming Project 8 from Chapter 5 so that the user enters a time using the 12hour clock.

The input will have the form hours:minutes followed by either A, P, AM, or PM (either lower-case or upper-ease).

White space is allowed (but not required) between the numerical time and the AM/PM indicator. Examples of valid input:

1:15P
1:15PM
1:15p
1:15pm
1:15 P
1:15 PM
1:15 p
1:15 pm

You may assume that the input has one of these forms; there is no need to test for errors.
 */

#include <ctype.h>
#include <stdio.h>

int main() {
    int hour, minute,
        offset,
        mins_since_midnight;
    char meridiem;

    printf("Enter a time(hh:mm am/pm): ");
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

    mins_since_midnight = ((hour + offset) * 60) + minute;

    if (mins_since_midnight <= ((8 * 60)))
        printf("Closest departure time is 8:00 a.m., arriving at 10:16 a.m.");
    else if (mins_since_midnight < ((9 * 60) + 43))
        printf("Closest departure time is 9:43 a.m., arriving at 11:52 a.m.");
    else if (mins_since_midnight < ((11 * 60) + 19))
        printf("Closest departure time is 11:19 a.m., arriving at 1:31 p.m.");
    else if (mins_since_midnight <= ((12 * 60) + 47))
        printf("Closest departure time is 12:47 p.m., arriving at 3:00 p.m.");
    else if (mins_since_midnight <= ((14 * 60)))
        printf("Closest departure time is 2:00 p.m., arriving at 4:08 p.m.");
    else if (mins_since_midnight <= ((15 * 60) + 45))
        printf("Closest departure time is 3:45 p.m., arriving at 5:55 p.m.");
    else if (mins_since_midnight <= ((19 * 60)))
        printf("Closest departure time is 7:00 p.m., arriving at 9:20 p.m.");
    else
        printf("Closest departure time is 9:45 p.m., arriving at 11:58 p.m.");

    return 0;
}

// Enter a 24-hour time (hh:mm): 1:25 pm
// Closest departure time is 2:00 p.m., arriving at 4:08 p.m.
