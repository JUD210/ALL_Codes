/* Write a program that takes a first name and last name entered by the user and displays the last name, a comma, and the first initial, followed by a period:

Enter a first and last name:  Lloyd Fosdick  (input)
Fosdick, L.

The user's input may contain extra Spaces before the first name, between the first and last names, and after the last name.
 */

#include <stdio.h>

int main() {
    char first_name_initial,
        ch;

    printf("Enter a first and last name: ");

    while ((ch = getchar()) == ' ')
        //Skip initial whitespace until first char
        ;
    first_name_initial = ch;

    while ((ch = getchar()) != ' ')
        // Skip chars after the first char until whitespace
        ;

    while ((ch = getchar()) != '\n') {
        if (ch != ' ')
            putchar(ch);
    }

    printf(", %c.", first_name_initial);

    return 0;
}

// Enter a first and last name: Lloyd Fosdick
// Fosdick, L.
