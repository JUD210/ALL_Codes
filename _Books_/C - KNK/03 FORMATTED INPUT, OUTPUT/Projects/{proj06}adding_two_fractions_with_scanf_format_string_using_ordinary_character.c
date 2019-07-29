/* Modify the addfrac.c program of Section 3.2 so that the user enters both fractions at the same time, separated by a plus sign:

Enter two fractions separated by a plus sign: 5/6+3/4 (input)
The sum is 38/24
*/

#include <stdio.h>

int main() {
    int nom1, denom1, nom2, denom2,
        result_nom, result_denom;

    printf("Enter two fractions separated by a plus sign: ");
    scanf("%d/%d+%d/%d", &nom1, &denom1, &nom2, &denom2);
    // Enter two fractions separated by a plus sign: 5/6+3/4

    result_nom = nom1 * denom2 + nom2 * denom1;
    result_denom = denom1 * denom2;
    printf("The sum is %d/%d\n", result_nom, result_denom);
    // The sum is 38/24

    return 0;
}
