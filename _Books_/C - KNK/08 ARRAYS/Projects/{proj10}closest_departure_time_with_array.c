/* Modify Programming Project 8 from Chapter 5 so that the departure times are stored in an array and the arrival times are stored in a second array. (The times are integers, representing the number of minutes since midnight.)

The program will use a loop to search the array of departure times for the one closest to the time entered by the user.
 */

#include <stdio.h>

#define NUM_OF_FLIGHTS 8

int main() {
    const int departure_times[NUM_OF_FLIGHTS] = {(8 * 60),
                                                 (9 * 60) + 43,
                                                 (11 * 60) + 19,
                                                 (12 * 60) + 47,
                                                 (14 * 60),
                                                 (15 * 60) + 45,
                                                 (19 * 60)};
    const int arrival_times[NUM_OF_FLIGHTS] = {(10 * 60) + 16,
                                               (11 * 60) + 52,
                                               (13 * 60) + 31,
                                               (15 * 60),
                                               (16 * 60) + 8,
                                               (17 * 60) + 55,
                                               (21 * 60) + 20,
                                               (23 * 60) + 58};

    int hour, minute, input_time;
    printf("Enter a 24-hour time (hh:mm): ");
    scanf("%2d:%2d", &hour, &minute);

    input_time = (hour * 60) + minute;

    for (int flight = 0; flight < NUM_OF_FLIGHTS; flight++) {
        if (departure_times[flight] >= input_time) {
            printf(
                "Closest departure time is %.2d:%.2d, "
                "arriving at %.2d:%.2d",
                departure_times[flight] / 60, departure_times[flight] % 60,
                arrival_times[flight] / 60, arrival_times[flight] % 60);
            break;
        }
    }

    // if (mins_since_midnight <= ((8 * 60)))
    //     printf("Closest departure time is 8:00 a.m., arriving at 10:16 a.m.");
    // else if (mins_since_midnight < ((9 * 60) + 43))
    //     printf("Closest departure time is 9:43 a.m., arriving at 11:52 a.m.");
    // else if (mins_since_midnight < ((11 * 60) + 19))
    //     printf("Closest departure time is 11:19 a.m., arriving at 1:31 p.m.");
    // else if (mins_since_midnight <= ((12 * 60) + 47))
    //     printf("Closest departure time is 12:47 p.m., arriving at 3:00 p.m.");
    // else if (mins_since_midnight <= ((14 * 60)))
    //     printf("Closest departure time is 2:00 p.m., arriving at 4:08 p.m.");
    // else if (mins_since_midnight <= ((15 * 60) + 45))
    //     printf("Closest departure time is 3:45 p.m., arriving at 5:55 p.m.");
    // else if (mins_since_midnight <= (19 * 60))
    //     printf("Closest departure time is 7:00 p.m., arriving at 9:20 p.m.");
    // else
    //     printf("Closest departure time is 9:45 p.m., arriving at 11:58 p.m.");

    return 0;
}
// Enter a 24-hour time (hh:mm): 13:25
// Closest departure time is 2:00 p.m., arriving at 4:08 p.m.
