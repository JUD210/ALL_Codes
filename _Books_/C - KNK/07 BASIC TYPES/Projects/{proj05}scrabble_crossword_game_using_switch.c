/* In the SCRABBLE Crossword Game, players form words using small tiles, each containing a letter and a face value. The face value varies from one letter to another, based on the letter's rarity. (Here are the face values: 1: AEILNORSTU, 2: DG, 3: BCMP, 4: FHVWY, 5: K, 8: JX, 9: QZ.)

Write a program that computes the value of a word by word_valueming the values of its letters:

Enter a word: pitfall (input)
Scrabble value: 12

Your program should allow any mixture of lower-case and upper-case letters in the word.
Hint: Use the toupper library Function.
 */

#include <ctype.h>
#include <stdio.h>

int main() {
    int word_value = 0;
    char ch;

    printf("Enter a word: ");

    while ((ch = getchar()) != '\n')
        switch (toupper(ch)) {
            case 'D':
            case 'G':
                word_value += 2;
                break;
            case 'B':
            case 'C':
            case 'M':
            case 'P':
                word_value += 3;
                break;
            case 'F':
            case 'H':
            case 'V':
            case 'W':
            case 'Y':
                word_value += 4;
                break;
            case 'K':
                word_value += 5;
                break;
            case 'J':
            case 'X':
                word_value += 8;
                break;
            case 'Q':
            case 'Z':
                word_value += 10;
                break;
            default:
                word_value++;
                break;
        }

    printf("Scrabble value: %d\n", word_value);

    return 0;
}

// Enter a word: example
// Scrabble value: 18
