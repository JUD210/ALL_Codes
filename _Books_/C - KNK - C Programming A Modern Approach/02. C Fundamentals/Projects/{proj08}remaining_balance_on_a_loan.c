/* Write a program that calculates the remaining balance on a loan after the first, second, and third monthly payments:

Enter amount of loan: 20000.00 (input)
Enter interest rate: 6.0 (input)
Enter monthly payment: 386.66 (input)

Balance remaining after first payment: $19713.34
Balance remaining after second payment: $19425.25
Balance remaining after third payment: $19135.71

Display each balance with two digits after the decimal point.

Hint: Each month, the balance is decreased by the amount of the payment, but increased by the balance times the monthly interest rate. To find the monthly interest rate, convert the interest rate entered by the user to a percentage and divide it by 12.

 */

#include <stdio.h>

int main()
{
  float amount_of_loan, interest_rate, monthly_payment;

  printf("Enter amount of loan: ");
  scanf("%f", &amount_of_loan);
  printf("Enter interest rate (percent): ");
  scanf("%f", &interest_rate);
  printf("Enter monthly payment: ");
  scanf("%f", &monthly_payment);
  // Enter amount of loan: 20000.00
  // Enter interest rate (percent): 6.0
  // Enter monthly payment: 386.66

  float monthly_interest_rate = interest_rate / 100 / 12;
  float balance = amount_of_loan;

  balance = balance * (1 + monthly_interest_rate) - monthly_payment;
  printf("Balance remaining after first payment: $%.2f\n", balance);
  // Balance remaining after first payment: $19713.34

  balance = balance * (1 + monthly_interest_rate) - monthly_payment;
  printf("Balance remaining after second payment: $%.2f\n", balance);
  // Balance remaining after second payment: $19425.25

  balance = balance * (1 + monthly_interest_rate) - monthly_payment;
  printf("Balance remaining after third payment: $%.2f", balance);
  // Balance remaining after third payment: $19135.71

  return 0;
}
