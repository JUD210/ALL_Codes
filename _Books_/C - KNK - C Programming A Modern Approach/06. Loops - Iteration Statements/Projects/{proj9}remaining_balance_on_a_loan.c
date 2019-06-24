/* Programming Project 8 in Chapter 2 asked you to write a program that calculates the remaining balance on a loan after the f‌irst, second, and third monthly payments. Modify the program so that it also asks the user to enter the number of payments and then displays the balance remaining after each of these payments. */

#include <stdio.h>

int main()
{
  float amount_of_loan, interest_rate, monthly_payment;
  int number_of_payments;

  printf("Enter amount of loan: ");
  scanf("%f", &amount_of_loan);
  printf("Enter interest rate (percent): ");
  scanf("%f", &interest_rate);
  printf("Enter monthly payment: ");
  scanf("%f", &monthly_payment);
  // Enter amount of loan: 20000.00
  // Enter interest rate (percent): 6.0
  // Enter monthly payment: 386.66

  printf("Enter number of payments: ");
  scanf("%d", &number_of_payments);
  // Enter number of payments: 5

  float monthly_interest_rate = interest_rate / 100 / 12;
  float balance = amount_of_loan;

  for (int i = 0; i < number_of_payments; i++)
  {
    balance = balance * (1 + monthly_interest_rate) - monthly_payment;
    printf("Balance remaining after %d payment: $%.2f\n", i + 1, balance);
  }
  // Balance remaining after 1 payment: $19713.34
  // Balance remaining after 2 payment: $19425.25
  // Balance remaining after 3 payment: $19135.71
  // Balance remaining after 4 payment: $18844.73
  // Balance remaining after 5 payment: $18552.29

  return 0;
}
