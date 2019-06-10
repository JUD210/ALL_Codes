/* Write a program that asks the user to enter a dollars-and-cents amount, then displays the amount with 5% tax added: 

Enter an amount: 100.00 (input)
With tax added: $105.00

*/

#include <stdio.h>

int main()
{
  float original_amount, amount_with_tax;

  printf("Enter an amount: ");
  scanf("%f", &original_amount);
  amount_with_tax = original_amount * 1.05f;
  printf("With tax added: $%.2f\n", amount_with_tax);

  return 0;
}