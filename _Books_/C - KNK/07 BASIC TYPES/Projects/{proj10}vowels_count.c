/* Write a program that counts the number of vowels (a, e, i, o, and u) in a sentence:

Enter a sentence: And that's the way it is. (input)
Your sentence contains 6 vowels.
 */

#include <ctype.h>
#include <stdio.h>

int main() {
    int vowels_count = 0;
    char ch;

    printf("Enter a sentence: ");
    while ((ch = getchar()) != '\n') {
        switch (toupper(ch)) {
            case 'A':
            case 'E':
            case 'I':
            case 'O':
            case 'U':
                vowels_count++;
                break;
        }
    }

    printf("Your sentence contains %d vowels.", vowels_count);

    return 0;
}

// Enter a sentence: And that's the way it is.
// Your sentence contains 6 vowels.
