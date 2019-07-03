/* Rearrange the square3.c program so that the for loop initializes i, tests i, and increments i. Don't rewrite the program: in particular, don't use any multiplications. */

#include <stdio.h>

int main()
{
  int i, n, odd, square;

  printf("This program prints a table of squares.\n");
  printf("Enter number of entries in table: ");
  scanf("%d", &n);
  // This program prints a table of squares.
  // Enter number of entries in table: 5

  for (i = 1, odd = 3, square = 1;
       i <= n;
       i++, square += odd, odd += 2)
  {
    printf("%10d%10d\n", i, square);
  }
  //          1         1
  //          2         4
  //          3         9
  //          4        16
  //          5        25

  return 0;
}
