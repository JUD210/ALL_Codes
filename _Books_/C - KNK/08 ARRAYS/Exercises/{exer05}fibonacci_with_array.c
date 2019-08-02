/* The Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13, where each number is the sum of the two preceding numbers.

Write a program fragment that declares an array named fib_numbers of length 40 and fills the array with the first 40 Fibonacci numbers.

Hint: Fill in the first two numbers individually, then use a loop to compute the remaining numbers.
 */

#include <stdio.h>

int main() {
    long fib_numbers[40] = {0, 1};
    printf("[0] %ld\n", fib_numbers[0]);
    printf("[1] %ld\n", fib_numbers[1]);

    for (int i = 2; i < 40; i++) {
        fib_numbers[i] = fib_numbers[i - 1] + fib_numbers[i - 2];
        printf("[%d] %ld\n", i, fib_numbers[i]);
    }

    return 0;
}

// [0] 0
// [1] 1
// [2] 1
// [3] 2
// [4] 3
// [5] 5
// [6] 8
// [7] 13
// [8] 21
// [9] 34
// [10] 55
// [11] 89
// [12] 144
// [13] 233
// [14] 377
// [15] 610
// [16] 987
// [17] 1597
// [18] 2584
// [19] 4181
// [20] 6765
// [21] 10946
// [22] 17711
// [23] 28657
// [24] 46368
// [25] 75025
// [26] 121393
// [27] 196418
// [28] 317811
// [29] 514229
// [30] 832040
// [31] 1346269
// [32] 2178309
// [33] 3524578
// [34] 5702887
// [35] 9227465
// [36] 14930352
// [37] 24157817
// [38] 39088169
// [39] 63245986
