/* The prototypical Internet newbie is a fellow named B1FF, who has a unique way of writing messages. Here's a typical B1FF communiqué:

H3Y DUD3, C 15 R1LLY C00L!!!!!!!!!!

Write a "B1FF filter" that reads a message entered by the user and translates it into B1FF-speak:

Enter message: Hey dude, C is rilly cool (input)
In B1FF-speak: H3Y DUD3, C 15 R1LLY C00L!!!!!!!!!!

Your program should convert the message to upper-case letters, substitute digits for certain letters (A->4, B->8, E->3, I->1, O->0, S->5), and then append 10 or so exclamation marks.

Hint: Store the original message in an array of characters, then go back through the array, translating and printing characters one by one.
 */

#include <ctype.h>
#include <stdio.h>
#define MSG_LEN 1000

int main() {
    char msg[MSG_LEN] = {};
    char ch;

    int index = 0;
    printf("Enter message: ");
    while ((ch = getchar()) != '\n') {
        msg[index] = ch;
        index++;
    }

    printf("In B1FF-speak: ");
    for (int i = 0; msg[i]; i++) {
        // if msg[i] is not null

        ch = toupper(msg[i]);
        switch (ch) {
            case 'A':
                ch = '4';
                break;
            case 'B':
                ch = '8';
                break;
            case 'E':
                ch = '3';
                break;
            case 'I':
                ch = '1';
                break;
            case 'O':
                ch = '0';
                break;
            case 'S':
                ch = '5';
                break;
            default:
                break;
        }
        putchar(ch);
    }
    printf("!!!!!!!!!!");

    return 0;
}

// Enter message: Hey dude, C is rilly cool
// In B1FF-speak: H3Y DUD3, C 15 R1LLY C00L!!!!!!!!!!
