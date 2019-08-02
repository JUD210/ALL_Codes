/*********************************************************
 * From C PROGRAMMING: A MODERN APPROACH, Second Edition *
 * By K. N. King                                         *
 * Copyright (c) 2008, 1996 W. W. Norton & Company, Inc. *
 * All rights reserved.                                  *
 * This program may be freely distributed for class use, *
 * provided that this copyright notice is retained.      *
 *********************************************************/

/* reverse2.c (Chapter 8, page 174) */
/* Reverses a series of numbers using a variable-length
   array - C99 only */

#include <stdio.h>

int main() {
    int i, n;

    printf("How many numbers do you want to reverse? ");
    scanf("%d", &n);

    int a[n]; /* C99 only - length of array depends on n */

    printf("Enter %d numbers: ", n);
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);

    printf("In reverse order:");
    for (i = n - 1; i >= 0; i--)
        printf(" %d", a[i]);
    printf("\n");

    return 0;
}

// How many numbers do you want to reverse? 10
// Enter 10 numbers: 34 82 49 102 7 94 23 11 50 31
// In reverse order: 31 50 11 23 94 7 102 49 82 34

// How many numbers do you want to reverse? 5
// Enter 5 numbers: 1 2 3 4 5 6
// In reverse order: 5 4 3 2 1
