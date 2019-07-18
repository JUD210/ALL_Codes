/* Use typedef to create types named Int8, Int16, and Int32. Define the types so that they represent 8-bit, 16-bit, and 32-bit integers on your machine. */

//! Refer 7.6.1 The sizeof Operator.txt

#include <stdint.h>
#include <stdio.h>

int main() {
    typedef int8_t Int8;
    typedef int16_t Int16;
    typedef int32_t Int32;

    //! %zu is used in C99.
    printf("Size of int8: %zu byte (%zu bits).\n", sizeof(Int8), sizeof(Int8) * 8);
    printf("Size of int16: %zu bytes (%zu bits).\n", sizeof(Int16), sizeof(Int16) * 8);
    printf("Size of int32: %zu bytes (%zu bits).\n", sizeof(Int32), sizeof(Int32) * 8);

    return 0;
}
