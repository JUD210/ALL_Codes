/* The following table shows the daily flights from one city to another:

Departure time   Arrival time
  8:00 a.m.      10:16 a.m.
  9:43 a.m.      11:52 a.m.
 11:19 a.m.       1:31 p.m.
 12:47 p.m.       3:00 p.m.
  2:00 p.m.       4:08 p.m.
  3:45 p.m.       5:55 p.m.
  7:00 p.m.       9:20 p.m.
  9:45 p.m.      11:58 p.m.

Write a program that asks the user to enter a time (expressed in
hours and minutes, using the 24-hour clock). The program then
displays the departure and arrival times for the flight whose
departure time is closest to that entered by the user:

Enter a 24-hour time: 13:25 (input)
Closest departure time is 12:47 p.m., arriving at 3:00 p.m.

Hint: Convert the input into a time expressed in minutes since
midnight, and compare it to the departure times, also expressed in
minutes since midnight.

For example, 13:15 is 13 x 60 + 15 = 795 minutes since midnight, which is closer to 12:47 p.m. (767 minutes since midnight) than to any of the other departure times.
 */

#include <stdio.h>

int main()
{
  int input_time, hours, minute,
      departure_time1 = 8 * 60 + 00, time_diff1,
      departure_time2 = 9 * 60 + 43, time_diff2,
      departure_time3 = 11 * 60 + 19, time_diff3,
      departure_time4 = 12 * 60 + 47, time_diff4,
      departure_time5 = 14 * 60 + 00, time_diff5,
      departure_time6 = 15 * 60 + 45, time_diff6,
      departure_time7 = 19 * 60 + 00, time_diff7,
      departure_time8 = 21 * 60 + 45, time_diff8,
      closest;

  printf("Enter a 24-hour time: ");
  scanf("%d:%d", &hours, &minute);
  // Enter a 24-hour time: 13:25 (input)

  input_time = hours * 60 + minute;

  time_diff1 =
      departure_time1 - input_time >= 0 ? departure_time1 - input_time : -(departure_time1 - input_time);
  time_diff2 =
      departure_time2 - input_time >= 0 ? departure_time2 - input_time : -(departure_time2 - input_time);
  time_diff3 =
      departure_time3 - input_time >= 0 ? departure_time3 - input_time : -(departure_time3 - input_time);
  time_diff4 =
      departure_time4 - input_time >= 0 ? departure_time4 - input_time : -(departure_time4 - input_time);
  time_diff5 =
      departure_time5 - input_time >= 0 ? departure_time5 - input_time : -(departure_time5 - input_time);
  time_diff6 =
      departure_time6 - input_time >= 0 ? departure_time6 - input_time : -(departure_time6 - input_time);
  time_diff7 =
      departure_time7 - input_time >= 0 ? departure_time7 - input_time : -(departure_time7 - input_time);
  time_diff8 =
      departure_time8 - input_time >= 0 ? departure_time8 - input_time : -(departure_time8 - input_time);

  /* Route 1. Beginner: Hard-coding with comparison

  // if it == 512
  //
  //  dt | td
  // ----|----
  // 100 | 412
  // 200 | 312
  // 300 | 212
  // 400 | 112
  // 500 | 12   <- C (12 < 88)
  // 600 | 88
  // 700 | 188
  // 800 | 288

  // if it == 190
  //
  //  dt | td
  // ----|----
  // 100 | 90
  // 200 | 10   <- C (10 < 110)
  // 300 | 110
  // 400 | 210
  // 500 | 310
  // 600 | 410
  // 700 | 510
  // 800 | 610

  */

  if (time_diff1 < time_diff2)
    printf("Closest departure time is  8:00 a.m., arriving at 10:16 a.m.\n");
  else if (time_diff2 < time_diff3)
    printf("Closest departure time is  9:43 a.m., arriving at 11:52 a.m.\n");
  else if (time_diff3 < time_diff4)
    printf("Closest departure time is 11:19 a.m., arriving at  1:31 p.m.\n");
  else if (time_diff4 < time_diff5)
    printf("Closest departure time is 12:47 p.m., arriving at  3:00 p.m.\n");
  else if (time_diff5 < time_diff6)
    printf("Closest departure time is  2:00 p.m., arriving at  4:08 p.m.\n");
  else if (time_diff6 < time_diff7)
    printf("Closest departure time is  3:45 p.m., arriving at  5:55 p.m.\n");
  else if (time_diff7 < time_diff8)
    printf("Closest departure time is  7:00 p.m., arriving at  9:20 p.m.\n");
  else
    printf("Closest departure time is  9:45 p.m., arriving at 11:58 p.m.\n");

  // Closest departure time is 12:47 p.m., arriving at 3:00 p.m.

  printf("%d\n", time_diff1);
  printf("%d\n", time_diff2);
  printf("%d\n", time_diff3);
  printf("%d\n", time_diff4);
  printf("%d\n", time_diff5);
  printf("%d\n", time_diff6);
  printf("%d\n", time_diff7);
  printf("%d\n", time_diff8);
  // 325
  // 222
  // 126
  // 38
  // 35   // This is the closest departure_time with input_time
  // 140
  // 335
  // 500

  /* Route 2. Advanced: Using array, iteration (sorting)

  // 4 3 2 1 0 1 2 3
  //
  // 3 4
  //     1 2
  //         0 1
  //             2 3
  // 1   3
  //         0   2
  // 0       1
  //
  // 0 . . . . . . .

  */

  return 0;
}