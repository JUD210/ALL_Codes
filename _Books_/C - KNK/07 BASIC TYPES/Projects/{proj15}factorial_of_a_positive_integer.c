/* Write a program that computes the factorial of a positive integer:

Enter a positive integer: 6 (input)
Factorial of 6: 720

(a) Use a short variable to store the value of the factorial. What is the largest value of n for which the program correctly prints the factorial of n?

(b) Repeat part (a), using an int variable instead.

(c) Repeat part (a), using a long variable instead.

(d) Repeat part (a), using a long long variable instead (if your compiler supports the long long type).

(e) Repeat part (a), using a float variable instead.

(f) Repeat part (a), using a double variable instead.

(g) Repeat part (a), using a long double variable instead.

In cases (e)-(g), the program will display a close approximation of the factorial, not necessarily the exact value.
 */

#include <stdio.h>

int main() {
    int num;

    short factorial_short = 1;
    int factorial_int = 1;
    long factorial_long = 1;
    long long factorial_long_long = 1;
    float factorial_float = 1;
    double factorial_double = 1;
    long double factorial_long_double = 1;

    printf("Enter a positive integer: ");
    scanf("%d", &num);

    printf("Factorial of %d: \n", num);

    for (int i = 1; i <= num; i++) {
        factorial_short *= i;
        factorial_int *= i;
        factorial_long *= i;
        factorial_long_long *= i;
        factorial_float *= i;
        factorial_double *= i;
        factorial_long_double *= i;

        printf("=== [%d!] === \n", i);

        printf("short: %hd\n", factorial_short);
        printf("int: %d\n", factorial_int);
        printf("long: %ld\n", factorial_long);
        printf("long long: %lld \n\n", factorial_long_long);

        printf("float: %e (%f)\n",
               factorial_float, factorial_float);
        printf("double: %e (%lf)\n\n",
               factorial_double, factorial_double);

        printf("long double: %Lf\n\n", factorial_long_double);
    }

    return 0;
}

/* On 32bit gcc

(a) Largest value of n that correctly prints its factorial (short): 7
(b) Largest value of n that correctly prints its factorial (int): 12
(c) Largest value of n that correctly prints its factorial (long): 12
(d) Largest value of n that correctly prints its factorial (long long): 12
(e) Largest value of n that correctly prints its factorial (float): 34
(f) Largest value of n that correctly prints its factorial (double): 170

(g) Largest value of n that correctly prints its factorial (long double): 1754
//...? I just get 0.000000 ONLY. maybe 64bit version gcc is needed.)
 */

/*

Enter a positive integer: 171
Factorial of 5:
=== [1!] ===
short: 1
int: 1
long: 1
long long: 1

float: 1.000000e+000 (1.000000)
double: 1.000000e+000 (1.000000)

long double: 0.000000

=== [2!] ===
short: 2
int: 2
long: 2
long long: 2

float: 2.000000e+000 (2.000000)
double: 2.000000e+000 (2.000000)

long double: 0.000000

//... (skip)

=== [170!] ===
short: 0
int: 0
long: 0
long long: 0

float: 1.#INF00e+000 (1.#INF00)
double: 7.257416e+306 (7257415615307994000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.000000)

long double: 0.000000

=== [171!] ===
short: 0
int: 0
long: 0
long long: 0

float: 1.#INF00e+000 (1.#INF00)
double: 1.#INF00e+000 (1.#INF00)
 */
