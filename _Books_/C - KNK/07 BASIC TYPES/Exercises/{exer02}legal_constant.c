/* Which of the following are not legal constants in C? Classify each legal constant as either integer or floating-point.
(a) 010E2
(b) 32.1E+5
(c) 3.978e-2
(d) 0790
(e) 100_000
 */

#include <stdio.h>

int man() {
    printf("%e (%f)\n", 010E2, 010E2);
    // 1.000000e+003 (1000.000000)
    /* This is a legal floating constant but slightly misleading. As it starts with a zero one might assume that it is in octal, but because
    this constant has an exponent it must be in base 10.
    This represents 10 * 10^2 (1,000).
     */

    ////////////////////////////////

    printf("%e (%f)\n", 32.1E+5, 32.1E+5);
    // 3.210000e+006 (3210000.000000)
    /* This is a legal floating constant with the value representing
    32.1 * 10^5 (3,210,000)
     */

    ////////////////////////////////

    printf("%e (%f)\n", 3.978e-2, 3.978e-2);
    // 3.978000e-002 (0.039780)
    /* This is a legal floating constant with the value representing
    3.978 * 10^-2 (0.03978)
     */

    ////////////////////////////////

    /* printf("%o\n", 0790); */
    // ERROR: invalid octal digit
    /* This isn't a legal constant because it starts with a 0 indicating
    that it is in base 8 (octal), but contains the digit 9. Octal
    numbers can only be represented by the values 0-7.
     */

    ////////////////////////////////

    /* printf("%d\n", 100_000); */
    // ERROR: extra text after expected end of number
    /* This constant is not legal as neither an integer or floating
    point value can contain an underscore. */

    /*
    With Python 3.6 (and PEP-515) there is a new convenience notation for big numbers introduced wh  ich allows you to divide groups of digits in the number literal so tha    t it is easier to read them.

    Examples of use:

        a = 1_00_00  # you do not need to group digits by 3!
        b = 0xbad_c0ffee  # you can make fun with hex digit notation
        c = 0b0101_01010101010_0100  # works with binary notation
        f = 1_000_00.0

        print(a,b,c,f, sep="\n")
        # 10000
        # 50159747054
        # 174756
        # 100000.0
     */

    return 0;
}