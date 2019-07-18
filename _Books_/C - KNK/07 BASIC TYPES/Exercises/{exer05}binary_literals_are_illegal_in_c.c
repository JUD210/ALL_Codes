/* Which of the following is not a legal way to write the number 65? (Assume
that the character set is ASCII.)

(a) 'A'
(b) 0b1000001
(c) 0101
(d) 0x41
 */

#include <stdio.h>

int main() {
    printf("%d\n", 'A');
    // 65

    ////////////////////////////////////

    printf("%d\n", 0b1000001);
    // 65
    /*
    (b) is not legal as C doesn't allow us to write binary literals,
    even though the number 1000001 is 65 in binary it isn't legal in C.

    Btw, even though it's not in standard C, but GCC supports it as an extension, prefixed by 0b or 0B.

    That's the reason why 65 was printed without no issue.
     */

    ////////////////////////////////////

    printf("%d\n", 0101);
    // 65

    ////////////////////////////////////

    printf("%d\n", 0x41);
    // 65

    ////////////////////////////////////

    return 0;
}
