/* Modify Programming Project 11 from Chapter 7 so that the program labels its output:

Enter a first and last name: Lloyd Fosdick (input)
You entered the name: Fosdick, L.

The program will need to store the last name (but not the first name) in an array of characters until it can be printed.

You may assume that the last name is no more than 20 characters long.
 */
#include <stdio.h>

#define last_name_limit 20

int main() {
    char last_name[last_name_limit];
    char first_initial;

    char ch;
    int i;

    printf("Enter a first and last name: ");

    while ((ch = getchar()) == ' ')
        // Skip initial whitespace until first char
        ;
    first_initial = ch;

    while ((ch = getchar()) != ' ')
        // Skip chars after the first char until whitespace
        ;

    i = 0;
    while ((ch = getchar()) != '\n') {
        last_name[i] = ch;
        i++;
    }

    printf("You entered the name: ");
    for (i = 0; last_name[i]; i++) {
        // if last_name[i] is empty, stop iteration.
        printf("%c", last_name[i]);
    }

    printf(", %c.", first_initial);

    return 0;
}

// Enter a first and last name: Lloyd Fosdick
// You entered the name: Fosdick, L.
