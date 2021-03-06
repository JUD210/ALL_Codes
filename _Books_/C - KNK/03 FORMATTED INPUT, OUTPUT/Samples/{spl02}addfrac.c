/*********************************************************
 * From C PROGRAMMING: A MODERN APPROACH, Second Edition *
 * By K. N. King                                         *
 * Copyright (c) 2008, 1996 W. W. Norton & Company, Inc. *
 * All rights reserved.                                  *
 * This program may be freely distributed for class use, *
 * provided that this copyright notice is retained.      *
 *********************************************************/

/* addfrac.c (Chapter 3, page 46) */
/* Adds two fractions */

#include <stdio.h>

int main() {
    int nom1, denom1, nom2, denom2,
        result_nom, result_denom;

    printf("Enter first fraction: ");
    scanf("%d/%d", &nom1, &denom1);
    // Enter first fraction: 5/6

    printf("Enter second fraction: ");
    scanf("%d/%d", &nom2, &denom2);
    // Enter second fraction: 3/4

    result_nom = nom1 * denom2 + nom2 * denom1;
    result_denom = denom1 * denom2;
    printf("The sum is %d/%d\n", result_nom, result_denom);
    // The sum is 38/24

    return 0;
}
