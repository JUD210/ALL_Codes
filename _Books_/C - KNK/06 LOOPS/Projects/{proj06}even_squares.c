/* Write a program that prompts the user to enter a number n, then prints all even squares between 1 and n. For example, if the user enters 100, the program should print the following:

4
16
36
64
100 */

#include <stdio.h>

int main() {
    int n;

    printf("Enter limit on maximum square: ");
    scanf("%d", &n);
    // Enter limit on maximum square: 100

    for (int i = 2, square = i * i;
         square <= n;
         i += 2, square = i * i) {
        printf("%d\n", square);
    }
    // 4
    // 16
    // 36
    // 64
    // 100

    // for (i = 2; i * i <= n; i += 2)
    //   printf("%d\n", i * i);

    return 0;
}