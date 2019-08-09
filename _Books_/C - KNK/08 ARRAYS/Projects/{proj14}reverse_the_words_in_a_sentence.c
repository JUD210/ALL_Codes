/* Write a program that reverses the words in a sentence:

Enter a sentence: you can cage a swallow can't you?
Reversal of sentence: you can't swallow a cage can you?

Hint: Use a loop to read the characters one by one and store them in a one-dimensional char array.

Have the loop stop at a period, question mark, or exclamation point (the "terminating character"), which is saved in a separate char variable.

Then use a second loop to search backward through the array for the beginning of the last word, Print the last word, then search backward for the next-to-last word.

Repeat until the beginning of the array is reached.

Finally, print the terminating character.
 */

#include <stdio.h>

#define sentence_limit 200

int main() {
    char sentence[sentence_limit];
    char terminating_char;

    char ch;
    int i, j, sentence_length, current_word_length;

    printf("Enter a sentence: ");

    i = 0;
    while ((ch = getchar()) != '\n') {
        if (ch == '.' || ch == '?' || ch == '!') {
            terminating_char = ch;
            sentence_length = i - 1;
            break;
        }

        sentence[i] = ch;
        i++;
    }

    printf("Reversal of sentence: ");

    // Iterate backwards through sentence array.
    for (i = sentence_length; i >= 0; i--) {
        // If we find a space, or we are at the start of the sentence we've found a new word.
        if (sentence[i] == ' ' || i == 0) {
            // Special case when we are at the start of the sentence, normally we iterate from i+1...word length to skip the white space, but the start of the sentence will have no preceding white space.
            if (i == 0) {
                i--;
            }

            // Iterate forwards over the word we found and print.

            // The reason why I'm adding 1 to current_word_length.
            // 1. when i != 0: to print ' '
            // 2. when i == 0: to print a final character of the current word
            for (j = i + 1; j <= i + current_word_length + 1; j++) {
                printf("%c", sentence[j]);
            }
            current_word_length = 0;
        } else {
            current_word_length++;
        }
    }

    printf("%c", terminating_char);

    return 0;
}

// Enter a sentence: you can cage a swallow can't you?
// Reversal of sentence: you can't swallow a cage can you?
