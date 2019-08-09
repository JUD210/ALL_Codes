/*********************************************************
 * From C PROGRAMMING: A MODERN APPROACH, Second Edition *
 * By K. N. King                                         *
 * Copyright (c) 2008, 1996 W. W. Norton & Company, Inc. *
 * All rights reserved.                                  *
 * This program may be freely distributed for class use, *
 * provided that this copyright notice is retained.      *
 *********************************************************/

/* countdown.c (Chapter 9, page 186) */
/* Prints a countdown */

#include <stdio.h>

void print_count(int n) {
    printf("T minus %d and counting\n", n);
}

int main() {
    int i;

    for (i = 10; i > 0; --i)
        print_count(i);

    return 0;
}

// T minus 10 and counting
// T minus 9 and counting
// T minus 8 and counting
// T minus 7 and counting
// T minus 6 and counting
// T minus 5 and counting
// T minus 4 and counting
// T minus 3 and counting
// T minus 2 and counting
// T minus 1 and counting
