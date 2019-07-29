/* Write a program that translates an alphabetic phone number into numeric form:

Enter phone number: CALLATT (input)
2255288

In case you don't have a telephone nearby, here are the letters on the keys:
       2=ABC, 3=DEF,
4=GHI, 5=JKL, 6=MNO,
7=PRS, 8=TUV, 9=WXY.

If the original phone number contains nonalphabetic characters (digits or punctuation, for example), leave them unchanged:

Enter phone number: 1-800-COL-LECT (input)
1-800-265-5328

You may assume that any letters entered by the user are upper-case.
 */

#include <ctype.h>
#include <stdio.h>

int main() {
    char ch;

    printf("Enter phone number: ");

    do {
        ch = getchar();
        ch = toupper(ch);

        //// This is standard.
        // switch (ch) {
        //     case 'A':
        //     case 'B':
        //     case 'C':
        //         printf("2");
        //         break;
        //     (skip)
        // }

        //// This is GCC extension, non-standard.
        // switch (ch) {
        //     case 'A' ... 'C':
        //         printf("2");
        //         break;
        //     (skip)
        // }

        //! And...
        //! THIS IS SPARTA!!
        if (ch >= 'A' && ch <= 'Y') {
            // ('A' or 'B' or 'C') - 'A' => (0 or 1 or 2) / 3 => 0 => print 2
            // ('D' or 'E' or 'F') - 'A' => (3 or 4 or 5) / 3 => 1 => print 3
            // (skip)
            printf("%d", ((ch - 'A') / 3) + 2);
        } else {
            printf("%c", ch);
        }
    } while (ch != '\n');

    return 0;
}

// Enter phone number: 1-800-COL-LECT
// 1-800-265-5328
