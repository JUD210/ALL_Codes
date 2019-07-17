/* The following "prime-testing" loop appeared in Section 6.4 as an example:

for (d = 2; d < n; d++)
  if (n % d == 0)
    goto done;
done:
if (d < n)
  printf("%d is not prime because it is divisible by %d\n", n, d);
else
  printf("%d is prime\n", n);


This loop isn't very eff‌icient. it's not necessary to divide n by all numbers between 2 and n - 1 to determine whether it's prime. In fact, we need only check divisors up to the square root of n.

Modify the loop to take advantage of this fact.

Hint: Don't try to compute the square root of 11; instead, compare d * d with n. */

#include <stdio.h>

int main() {
    int d, n;

    for (n = 2; n < 15; n++) {
        for (d = 2; d * d <= n; d++) {
            if (n % d == 0)
                break;
        }

        if (d * d <= n)
            printf("%d is not prime because it is divisible by %d\n", n, d);
        else
            printf("%d is prime\n", n);
        // 2 is prime
        // 3 is prime
        // 4 is not prime because it is divisible by 2
        // 5 is prime
        // 6 is not prime because it is divisible by 2
        // 7 is prime
        // 8 is not prime because it is divisible by 2
        // 9 is not prime because it is divisible by 3
        // 10 is not prime because it is divisible by 2
        // 11 is prime
        // 12 is not prime because it is divisible by 2
        // 13 is prime
        // 14 is not prime because it is divisible by 2

        ////////////////////////////////////////////////////////////

        // for (d = 2; d < n; d++)
        //   if (n % d == 0)
        //     goto done;
        // done:
        // if (d < n)
        //   printf("%d is not prime because it is divisible by %d\n", n, d);
        // else
        //   printf("%d is prime\n", n);
    }

    return 0;
}