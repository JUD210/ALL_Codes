#include <conio.h>
#include <stdbool.h>
#include <stdio.h>
#include <time.h>
#include <windows.h>  // system("pause");

#define COLOR_RED "\x1b[31m"
#define COLOR_GREEN "\x1b[32m"
#define COLOR_YELLOW "\x1b[33m"
#define COLOR_BLUE "\x1b[34m"
#define COLOR_MAGENTA "\x1b[35m"
#define COLOR_CYAN "\x1b[36m"

#define COLOR_RESET "\x1b[0m"

int main() {
    time_t my_time;
    struct tm* timeinfo;
    int year, mon, day, hour, min, sec;

    time(&my_time);
    timeinfo = localtime(&my_time);

    year = timeinfo->tm_year + 1900;
    mon = timeinfo->tm_mon + 1;
    day = timeinfo->tm_mday;
    hour = timeinfo->tm_hour;
    min = timeinfo->tm_min;
    sec = timeinfo->tm_sec;

    printf("========================================================\n");
    printf("\x1b[1m" COLOR_CYAN "%.4d/%.2d/%.2d %.2d:%.2d:%.2d\n" COLOR_RESET,
           year, mon, day, hour, min, sec);

    printf("========================================================\n");
    printf(COLOR_CYAN "What are doing now?\n" COLOR_RESET);
    printf(COLOR_CYAN "Be honest " COLOR_RED "100%%" COLOR_CYAN
                      ", and tell me.\n" COLOR_RESET);

    printf("========================================================\n");
    printf("According to plan,\n\n");
    if (hour >= 7 && hour < 22) {
        printf("its %.2d:%.2d (7H ~ 22H) now,\n", hour, min);
        printf("so you MUST stream Dev/Study right now!\n");
    } else if (hour >= 22 && hour < 24) {
        printf("its %.2d:%.2d (22H ~ 24H) now,\n", hour, min);
        printf("so you should take a break. You did a great job! :D\n");
    } else {
        printf("its %.2d:%.2d (0H ~ 7H) now,\n", hour, min);
        printf("so you MUST sleep right now. What are you doing!!! Just turn off everything!\n");
    }

    printf("========================================================\n");

    system("pause");
    return 0;
}