/* Give the decimal value of each of the following integer constants.
(a) 077
(b) 0x77
(c) OXABC
 */

#include <stdio.h>

int main() {
    printf(
        "%d\n"
        "%d\n"
        "%d\n",
        077,
        0x77,
        0XABC);
    // 63
    // 119
    // 2748
    printf("=====\n");

    printf(
        "%o\n"
        "%x\n"
        "%x or %X\n",
        63,
        119,
        2748, 2748);
    // 77
    // 77
    // abc or ABC

    return 0;
}