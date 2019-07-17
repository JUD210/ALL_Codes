/*********************************************************
 * From C PROGRAMMING: A MODERN APPROACH, Second Edition *
 * By K. N. King                                         *
 * Copyright (c) 2008, 1996 W. W. Norton & Company, Inc. *
 * All rights reserved.                                  *
 * This program may be freely distributed for class use, *
 * provided that this copyright notice is retained.      *
 *********************************************************/

/* tprintf.c (Chapter 3, page 40) */
/* Prints int and float values in various formats */

#include <stdio.h>

int main() {
    int i;
    float x, y;

    i = 40;
    x = 839.21f;
    y = 839.21;

    printf("|%d|%5d|%-5d|%5.3d|\n", i, i, i, i);
    printf("|%11.3f|%11.3e|%11g|\n", x, x, x);
    printf("|%-11.3f|%-11.3e|%-11g|\n", y, y, y);
    // |40|   40|40   |  040|
    // |    839.210| 8.392e+002|     839.21|
    // |839.210    |8.392e+002 |839.21     |

    return 0;
}
