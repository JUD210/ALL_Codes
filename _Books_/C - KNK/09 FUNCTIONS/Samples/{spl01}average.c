/*********************************************************
 * From C PROGRAMMING: A MODERN APPROACH, Second Edition *
 * By K. N. King                                         *
 * Copyright (c) 2008, 1996 W. W. Norton & Company, Inc. *
 * All rights reserved.                                  *
 * This program may be freely distributed for class use, *
 * provided that this copyright notice is retained.      *
 *********************************************************/

/* average.c (Chapter 9, page 185) */
/* Computes pairwise averages of three numbers */

#include <stdio.h>

double average(double a, double b) {
    return (a + b) / 2;
}

int main() {
    double x, y, z;

    printf("Enter three numbers: ");
    scanf("%lf%lf%lf", &x, &y, &z);

    printf("Average of %g and %g: %g\n", x, y, average(x, y));
    printf("Average of %.5g and %.5g: %.5g\n", y, z, average(y, z));
    printf("Average of %f and %f: %.2f\n", x, z, average(x, z));

    return 0;
}

// Enter three numbers: 3.0 9.6 10
// Average of 3 and 9.6: 6.3
// Average of 9.6 and 10: 9.8
// Average of 3.000000 and 10.000000: 6.50
