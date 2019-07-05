/*********************************************************
 * From C PROGRAMMING: A MODERN APPROACH, Second Edition *
 * By K. N. King                                         *
 * Copyright (c) 2008, 1996 W. W. Norton & Company, Inc. *
 * All rights reserved.                                  *
 * This program may be freely distributed for class use, *
 * provided that this copyright notice is retained.      *
 *********************************************************/

/* sum2.c (Chapter 7, page 131) */
/* Sums a series of numbers (using long variables) */

#include <stdio.h>

int main()
{
  long n, sum = 0;

  printf("This program sums a series of integers.\n");
  // This program sums a series of integers.

  printf("Enter integers (0 to terminate): ");
  scanf("%ld", &n);
  // Enter integers (0 to terminate): 10000 20000

  while (n != 0)
  {
    sum += n;
    scanf("%ld", &n);
  }
  // 30000 0

  printf("The sum is: %ld\n", sum);
  // The sum is: 60000

  return 0;
}
