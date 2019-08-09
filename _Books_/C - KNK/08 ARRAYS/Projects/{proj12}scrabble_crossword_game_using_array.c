/* Modify Programming Project 5 from Chapter 7 so that the SCRABBLE values of the letters are stored in an array. The array will have 26 elements, corresponding to the 26 letters of the alphabet.

For example, element 0 of the array will store 1 (because the SCRABBLE value of the letter A is 1). element 1 of the array will store 3 (because the SCRABBLE value of the letter B is 3), and so forth.

As each character of the input word is read, the program will use the array to determine the SCRABBLE value of that character.

Use an array initializer to setup the array.
 */

#include <ctype.h>
#include <stdio.h>

int main() {
    int word_value = 0;
    int scrabble_values[26] = {
    //  A  B  C  D  E  F  G  H  I  J  K  L  M
        1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
    //  N  O  P  Q   R  S  T  U  V  W  X  Y  Z
        1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    char ch;


    printf("Enter a word: ");

    while ((ch = getchar()) != '\n')
        word_value += scrabble_values[toupper(ch) - 'A'];

    printf("Scrabble value: %d", word_value);

    return 0;
}

// Enter a word: example
// Scrabble value: 18
