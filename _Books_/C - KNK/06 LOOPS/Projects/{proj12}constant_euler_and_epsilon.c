/* Modify Programming Project 11 so that the program continues adding terms until the current term becomes less than ε, where ε is a small (f‌loating-point) number entered by the user.

// epsilon = ε (Infinitesimal 무한소)
 */

#include <stdio.h>

int main() {
    int n, factorial;
    float euler, epsilon, term;

    printf("e = 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!\n");
    printf("program continues adding terms until the current term becomes less than epsilon\n");
    printf("Enter the value of epsilon: ");
    scanf("%f", &epsilon);
    // Enter the value of epsilon: 0.16

    euler = 1.0f;
    for (int i = 1;; i++) {
        factorial = 1;
        for (int j = 1; j <= i; j++) {
            factorial *= j;
        }
        term = 1.0f / factorial;

        if (term < epsilon)
            break;
        euler += term;
    }

    printf("e = %f", euler);
    // e = 2.666667

    return 0;
}