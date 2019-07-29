/* Modify the square2.c program of Section 6.3 so that it pauses after every 24 squares and displays the following message:

Press Enter to continue...

After displaying the message, the program should use getchar to read a character.

getchar won't allow the program to continue until the user presses the Enter key. */

#include <stdio.h>

int main() {
    int i, n;
    char ch;

    printf("This program prints a table of squares.\n");
    printf("Enter number of entries in table: ");
    scanf("%d", &n);

    while (getchar() != '\n')
        ;  // null statement

    /*
    Dispose of new-line character following number of entries.
    could simply be
        ch = getchar();
    or
        getchar();
     */

    for (i = 1; i <= n; i++) {
        printf("%10d%10d\n", i, i * i);
        if (i % 24 == 0) {
            printf("Press Enter to continue...");
            while (getchar() != '\n')
                ;
        }
    }

    return 0;
}

// This program prints a table of squares.
// Enter number of entries in table: 50
//          1         1
//          2         4
//          3         9
//          4        16
//          5        25
//          6        36
//          7        49
//          8        64
//          9        81
//         10       100
//         11       121
//         12       144
//         13       169
//         14       196
//         15       225
//         16       256
//         17       289
//         18       324
//         19       361
//         20       400
//         21       441
//         22       484
//         23       529
//         24       576
// Press Enter to continue...flaksdlksdflwef  asdlf awelf as d lksj sd fsdk j
//! If ch = getchar(); or getchar(); was used,
//! because of the whitespace character, next getchar() would be skipped.
//         25       625
//         26       676
//         27       729
//         28       784
//         29       841
//         30       900
//         31       961
//         32      1024
//         33      1089
//         34      1156
//         35      1225
//         36      1296
//         37      1369
//         38      1444
//         39      1521
//         40      1600
//         41      1681
//         42      1764
//         43      1849
//         44      1936
//         45      2025
//         46      2116
//         47      2209
//         48      2304
// Press Enter to continue...asdf
//         49      2401
//         50      2500