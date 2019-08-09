/* Modify Programming Project 4 from Chapter 7 so that the program labels its output:

Enter phone number: 1-800-COL-LECT (input)
In numeric form: 1-800-265-5328

The program will need to store the phone number (either in its original form or in its numeric form) in an array of characters until it can be printed.

You may assume that the phone number is no more than 15 characters long.
 */

#include <ctype.h>
#include <stdio.h>

#define NUMBER_LIMIT 15

int main() {
    char original_form[NUMBER_LIMIT];
    char numeric_form[NUMBER_LIMIT];

    printf("Enter phone number (15 char limit): ");

    for (int i = 0; i < NUMBER_LIMIT; i++) {
        char ch = toupper(getchar());
        original_form[i] = ch;

        if (ch >= 'A' && ch <= 'Y') {
            // ('A' or 'B' or 'C') - 'A' => (0 or 1 or 2) / 3 => 0 => print 2
            // ('D' or 'E' or 'F') - 'A' => (3 or 4 or 5) / 3 => 1 => print 3
            // (skip)
            numeric_form[i] = (((ch - 'A') / 3) + 2) + '0';
        } else {
            numeric_form[i] = ch;
        }
    }

    printf("In numeric form: ");
    for (int i = 0; i < NUMBER_LIMIT; i++) {
        printf("%c", numeric_form[i]);
    }

    return 0;
}

// Enter phone number (15 char limit): 1-800-COL-LECT
// In numeric form: 1-800-265-5328
