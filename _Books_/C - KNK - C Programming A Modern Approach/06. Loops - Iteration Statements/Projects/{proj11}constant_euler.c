/* The value of the mathematical constant e can be expressed as an inf‌inite series:

// euler = e (Euler's number 자연상수)

e = 1 + 1/1! + 1/2! + 1/3! + ...

Write a program that approximates e by computing the value of

1 + 1/1! + 1/2! + 1/3! + ... + 1/n!

where n is an integer entered by the user.
 */

#include <stdio.h>

int main()
{
  int n, factorial;
  float euler;

  printf("e = 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!\n");
  printf("Enter the value of n: ");
  scanf("%d", &n);
  // Enter the value of n: 3

  euler = 1.0f;
  for (int i = 1; i <= n; i++)
  {
    factorial = 1;
    for (int j = 1; j <= i; j++)
    {
      factorial *= j;
    }

    euler += 1.0f / factorial;
  }

  printf("e = %f", euler);
  // e = 2.666667  // 1 + 1 + 0.5 + 0.166667

  return 0;
}