/*********************************************************
 * From C PROGRAMMING: A MODERN APPROACH, Second Edition *
 * By K. N. King                                         *
 * Copyright (c) 2008, 1996 W. W. Norton & Company, Inc. *
 * All rights reserved.                                  *
 * This program may be freely distributed for class use, *
 * provided that this copyright notice is retained.      *
 *********************************************************/

/* square3.c (Chapter 6, page 110) */
/* Prints a table of squares using an odd method */

#include <stdio.h>

int main() {
    int i, n, odd, square;

    printf("This program prints a table of squares.\n");
    printf("Enter number of entries in table: ");
    scanf("%d", &n);
    // This program prints a table of squares.
    // Enter number of entries in table: 5

    i = 1;
    odd = 3;
    for (square = 1; i <= n; odd += 2) {
        printf("%10d%10d\n", i, square);
        ++i;
        square += odd;
    }
    //          1         1
    //          2         4
    //          3         9
    //          4        16
    //          5        25

    return 0;
}

/* The for loop would be a lot clearer if we rearranged its pieces so that the loop is clearly controlled by i. */