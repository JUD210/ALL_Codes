/* One of the oldest known encryption techniques is the Caesar cipher, attributed to Julius Caesar.

It involves replacing each letter in a message with another letter that is a fixed number of positions later in the alphabet. (If the replacement would go past the letter Z, the cipher "wraps around" to the beginning of the alphabet. For example, if each letter is replaced by the letter two positions after it, then Y would be replaced by A, and Z would be replaced by 8.)


Write a program that encrypts a message using a Caesar cipher. The user will enter the message to be encrypted and the shift amount (the number of positions by which letters should be shifted):

Enter message to be encrypted: Go ahead, make my day. (input)
Enter shift amount (1-25): 3 (input)
Encrypted message: Jr dkhdg, pdnh pb gdb.


Notice that the program can decrypt a message if the user enters 26 minus the original key:

Enter message to be encrypted: Jr dkhdg, pdnh pb gdb. (input)
Enter shift amount (1-25): 23 (input)
Encrypted message: Go ahead, make my day.


You may assume that the message does not exceed 80 characters. Characters other than letters should be left unchanged. Lower-case letters remain lower-case when encrypted, and upper-case letters remain upper-ease.

Hint: To handle the wrap-around problem, use the expression
((ch - 'A') + n) % 26 + 'A'
to calculate the encrypted version of an upper-case letter, where ch stores the letter and n stores the shift amount. (You'll need a similar expression for lower-case letters.)
 */

#include <stdio.h>

#define msg_limit 80

int main() {
    char msg[msg_limit];
    char ch;
    int shift_amount;

    printf("Enter message to be encrypted: ");
    for (int i = 0; ((ch = getchar()) != '\n'); i++) {
        msg[i] = ch;
    }

    // Can decrypt a message if the user enters 26 minus the original key
    printf("Enter shift amount (1-25): ");
    scanf("%d", &shift_amount);

    printf("Encrypted message: ");
    for (int i = 0; msg[i]; i++) {
        if (msg[i] >= 'a' && msg[i] <= 'z') {
            msg[i] = ((msg[i] - 'a') + shift_amount) % 26 + 'a';
        } else if (msg[i] >= 'A' && msg[i] <= 'Z') {
            msg[i] = ((msg[i] - 'A') + shift_amount) % 26 + 'A';
        }

        printf("%c", msg[i]);
    }

    return 0;
}

// Enter message to be encrypted: Go ahead, make my day. (input)
// Enter shift amount (1-25): 3 (input)
// Encrypted message: Jr dkhdg, pdnh pb gdb.

// Enter message to be encrypted: Jr dkhdg, pdnh pb gdb. (input)
// Enter shift amount (1-25): 23 (input)
// Encrypted message: Go ahead, make my day.
