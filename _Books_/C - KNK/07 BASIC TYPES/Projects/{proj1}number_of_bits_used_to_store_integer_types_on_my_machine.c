/* The square2.c program of Section 6.3 will fail (usually by printing strange answers) if i * i exceeds the maximum int value.

Run the program and determine the smallest value of n that causes failure.

Try changing the type of i to short and running the program again. (Don't forget to update the conversion specifications in the call of printf!) Then try long.

From these experiments, what can you conclude about the number of bits used to store integer types on your machine?
 */

#include <stdio.h>

int main() {
    for (short s = 170; s <= 190; s++)
        printf("%10hd%10hd\n", s, s * s);
    //// 2^15 - 1 = 32767 (16 bit)
    //        170     28900
    //        171     29241
    //        172     29584
    //        173     29929
    //        174     30276
    //        175     30625
    //        176     30976
    //        177     31329
    //        178     31684
    //        179     32041
    //        180     32400
    //        181     32761
    //!        182    -32412
    //        183    -32047
    //        184    -31680
    //        185    -31311
    //        186    -30940
    //        187    -30567
    //        188    -30192
    //        189    -29815
    //        190    -29436

    for (int i = 46330; i <= 46350; i++)
        printf("%10d%20d\n", i, i * i);
    //// 2^31 - 1 = 2147483647 (32 bit)
    //      46330          2146468900
    //      46331          2146561561
    //      46332          2146654224
    //      46333          2146746889
    //      46334          2146839556
    //      46335          2146932225
    //      46336          2147024896
    //      46337          2147117569
    //      46338          2147210244
    //      46339          2147302921
    //      46340          2147395600
    //!      46341         -2147479015
    //      46342         -2147386332
    //      46343         -2147293647
    //      46344         -2147200960
    //      46345         -2147108271
    //      46346         -2147015580
    //      46347         -2146922887
    //      46348         -2146830192
    //      46349         -2146737495
    //      46350         -2146644796

    for (long l = 46330; l <= 46350; l++)
        printf("%10ld%20ld\n", l, l * l);
    //// 2^31 - 1 (32 bit)
    //      46330          2146468900
    //      46331          2146561561
    //      46332          2146654224
    //      46333          2146746889
    //      46334          2146839556
    //      46335          2146932225
    //      46336          2147024896
    //      46337          2147117569
    //      46338          2147210244
    //      46339          2147302921
    //      46340          2147395600
    //!      46341         -2147479015
    //      46342         -2147386332
    //      46343         -2147293647
    //      46344         -2147200960
    //      46345         -2147108271
    //      46346         -2147015580
    //      46347         -2146922887
    //      46348         -2146830192
    //      46349         -2146737495
    //      46350         -2146644796

    // short int values are usually stored in 16 bits, causing failure at 182.
    // int and long int values are usually stored in 32 bits, with failure occurring at 46341.

    // Therefore, my c compiler (gcc) is running on 32bit mode (Even if my CPU is 64bit based).

    return 0;
}