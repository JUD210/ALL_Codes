/* Write a program that prints the values of

sizeof(int)
sizeof(short)
sizeof (long)
sizeof(float)
sizeof(double)
sizeof(long double)
 */

#include <stdio.h>

int main(void) {
    printf(
        "Size of int: %d(%%d from C89) | "
        "%zu(%%zu from C99)\n",
        (int)sizeof(int),
        sizeof(int));
    printf(
        "Size of short: %d(%%d from C89) | "
        "%zu(%%zu from C99)\n",
        (int)sizeof(short),
        sizeof(short));
    printf(
        "Size of long: %d(%%d from C89) | "
        "%zu(%%zu from C99)\n",
        (int)sizeof(long),
        sizeof(long));
    printf(
        "Size of float: %d(%%d from C89) | "
        "%zu(%%zu from C99)\n",
        (int)sizeof(float),
        sizeof(float));
    printf(
        "Size of double: %d(%%d from C89) | "
        "%zu(%%zu from C99)\n",
        (int)sizeof(double),
        sizeof(double));
    printf(
        "Size of long double: %d(%%d from C89) | "
        "%zu(%%zu from C99)\n",
        (int)sizeof(long double),
        sizeof(long double));

    ////////////////////////////////

    printf(
        "\n"
        "Size of 15+2.12 * 10: %lu(%%lu from C89) | "
        "%zu(%%zu from C99)\n",
        (unsigned long)sizeof(15 + 2.12 * 10),
        sizeof(15 + 2.12 * 10));

    return 0;
}

//! Since the type of a sizeof expression may vary from one implementation to another, it's necessary in C89 to cast sizeof expressions to a known type before printing them. The sizes of the basic types are small numbers, so it's safe to cast them to int. (In general, however, it's best to cast sizeof expressions to unsigned long and print them using %lu.)

//! In C99, we can avoid the cast by using the %zu conversion specification.
