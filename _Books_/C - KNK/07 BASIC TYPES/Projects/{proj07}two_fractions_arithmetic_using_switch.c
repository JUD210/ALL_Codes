/* Modify Programming Project 6 from Chapter 3 so that the user may add, subtract, multiply or divide two fractions at the same time (by entering either +, -, *, or / between the fractions). */

#include <stdio.h>

int main() {
    int nom1, denom1, nom2, denom2,
        result_nom, result_denom;
    char oper;

    printf("Enter two fractions separated by a +, -, *, or / sign: ");
    scanf("%d/%d", &nom1, &denom1);
    oper = getchar();
    scanf("%d/%d", &nom2, &denom2);

    switch (oper) {
        case '+':
            result_nom = nom1 * denom2 + nom2 * denom1;
            result_denom = denom1 * denom2;
            break;
        case '-':
            result_nom = nom1 * denom2 - nom2 * denom1;
            result_denom = denom1 * denom2;
            break;
        case '*':
            result_nom = nom1 * nom2;
            result_denom = denom1 * denom2;
            break;
        case '/':
            result_nom = nom1 * denom2;
            result_denom = nom2 * denom1;
            break;
    }

    printf("The result is %d/%d\n", result_nom, result_denom);

    return 0;
}

// Enter two fractions separated by a +, -, *, or / sign: 5/6 + 3/4
// The result is 38/24

// Enter two fractions separated by a +, -, *, or / sign: 5/6 - 3/4
// The result is 2/24

// Enter two fractions separated by a +, -, *, or / sign: 5/6 * 3/4
// The result is 15/24

// Enter two fractions separated by a +, -, *, or / sign: 5/6 / 3/4
// The result is 20/18
