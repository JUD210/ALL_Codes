/* Write a program that finds the largest and smallest of four integers entered by the user:

Enter four integers: 21 43 10 35 (input)
Largest: 43
Smallest: 10

Use as few if statements as possible.

Hint: Four if statements are suff‌icient. */

#include <stdio.h>

int main()
{
  int n1, n2, n3, n4,
      tmp;

  printf("Enter four integers: ");
  scanf("%d %d %d %d", &n1, &n2, &n3, &n4);
  // Enter four integers: 2 4 1 3

  // 4 3 2 1  |  2 4 1 3
  //          |
  // 3 4      |  2 4
  //     1 2  |      1 3
  // 1   3    |  1   2
  //   2   4  |    3   4
  //          |
  // 1 . . 4  |  1 . . 4

  if (n1 > n2)
  {
    tmp = n1;
    n1 = n2;
    n2 = tmp;
  }
  if (n3 > n4)
  {
    tmp = n3;
    n3 = n4;
    n4 = tmp;
  }
  if (n1 > n3)
  {
    tmp = n1;
    n1 = n3;
    n3 = tmp;
  }
  if (n2 > n4)
  {
    tmp = n2;
    n2 = n4;
    n4 = tmp;
  }

  printf("Largest: %d\n", n4);
  // Largest: 4

  printf("Smallest: %d\n", n1);
  // Smallest: 1

  return 0;
}