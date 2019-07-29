/* Write a program that calculates the average word length for a sentence:

Enter a sentence: It was deja vu all over again. (input)
Average word length: 3.4

For simplicity, your program should consider a punctuation mark to be part of the word to which it is attached. Display the average word length to one decimal place.
 */

#include <stdio.h>

int main() {
    int word_count = 0,
        character_count = 0;
    char ch;

    printf("Enter a sentence: ");
    while ((ch = getchar()) != '\n') {
        if (ch == ' ') {  //assume one space per word
            word_count++;
        } else {
            character_count++;
        }
    }

    word_count += 1;  //last word isn't counted due to break on \n, so increment by one.

    printf("Average word length: %.1f",
           (float)character_count / word_count);

    return 0;
}

// Enter a sentence: It was deja vu all over again.
// Average word length: 3.4
