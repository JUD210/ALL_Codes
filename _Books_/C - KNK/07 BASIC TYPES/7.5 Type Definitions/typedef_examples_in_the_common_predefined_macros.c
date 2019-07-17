#include <stdio.h>

int main() {
    /*
        https://gcc.gnu.org/onlinedocs/cpp/Common-Predefined-Macros.html

        __SIZE_TYPE__
        __PTRDIFF_TYPE__
        __WCHAR_TYPE__
        __WINT_TYPE__
        __INTMAX_TYPE__
        __UINTMAX_TYPE__
        __SIG_ATOMIC_TYPE__
        __INT8_TYPE__
        __INT16_TYPE__
        __INT32_TYPE__
        __INT64_TYPE__
        __UINT8_TYPE__
        __UINT16_TYPE__
        __UINT32_TYPE__
        __UINT64_TYPE__
        __INT_LEAST8_TYPE__
        __INT_LEAST16_TYPE__
        __INT_LEAST32_TYPE__
        __INT_LEAST64_TYPE__
        __UINT_LEAST8_TYPE__
        __UINT_LEAST16_TYPE__
        __UINT_LEAST32_TYPE__
        __UINT_LEAST64_TYPE__
        __INT_FAST8_TYPE__
        __INT_FAST16_TYPE__
        __INT_FAST32_TYPE__
        __INT_FAST64_TYPE__
        __UINT_FAST8_TYPE__
        __UINT_FAST16_TYPE__
        __UINT_FAST32_TYPE__
        __UINT_FAST64_TYPE__
        __INTPTR_TYPE__
        __UINTPTR_TYPE__

        These macros are defined to the correct underlying types for the size_t, ptrdiff_t, wchar_t, wint_t, intmax_t, uintmax_t, sig_atomic_t, int8_t, int16_t, int32_t, int64_t, uint8_t, uint16_t, uint32_t, uint64_t, int_least8_t, int_least16_t, int_least32_t, int_least64_t, uint_least8_t, uint_least16_t, uint_least32_t, uint_least64_t, int_fast8_t, int_fast16_t, int_fast32_t, int_fast64_t, uint_fast8_t, uint_fast16_t, uint_fast32_t, uint_fast64_t, intptr_t, and uintptr_t typedefs, respectively.

        They exist to make the standard header files stddef.h, stdint.h, and wchar.h work correctly. You should not use these macros directly; instead, include the appropriate headers and use the typedefs. Some of these macros may not be defined on particular systems if GCC does not provide a stdint.h header on those systems.
     */

    ////////////////////////////////////////////////////////////////////////

    // #define __int8 char
    // #define __INT8_TYPE__ signed char
    // #define __INT8_MAX__ 0x7f
    __int8 ch = __INT8_MAX__;
    __INT8_TYPE__ sch = __INT8_MAX__;

    // #define __UINT8_TYPE__ unsigned char
    // #define __UINT8_MAX__ 0xff
    __UINT8_TYPE__ uch = __UINT8_MAX__;

    printf(
        "ch: %d %c\n"
        "sch: %d %c\n"
        "uch: %d %c\n",
        ch, ch,
        sch, sch,
        uch, uch);
    // ch: 127
    // sch: 127
    // uch: 255 

    ////////////////////////////////////////////////////////////////////////

    // #define __int16 short
    // #define __INT16_TYPE__ short int
    // #define __INT16_MAX__ 0x7fff
    __int16 s = __INT16_MAX__;
    __INT16_TYPE__ si = __INT16_MAX__;

    // #define __UINT16_TYPE__ unsigned short int
    // #define __UINT16_MAX__ 0xffff

    /*
        ...
     */

    return 0;
}
