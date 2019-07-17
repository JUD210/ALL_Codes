/* Write a program that formats product information entered by the user. A session with the program should look like this:

Enter item number: 583 (input)
Enter unit price: 13.5 (input)
Enter purchase date (mm/dd/yyyy) : 10/24/2010 (input)

Item            Unit            Purchase
                Price           Date
583             $  13.50        10/24/2010

The item number and date should be left justified; the unit price should be right justified. Allow dollar amounts up to $9999.99.

Hint: Use tabs to line up the columns.

 */

#include <stdio.h>

int main() {
    int item_number, month, day, year;
    float unit_price;

    printf("Enter item number: ");
    scanf("%d", &item_number);
    printf("Enter unit price: ");
    scanf("%f", &unit_price);
    printf("Enter purchase date (mm/dd/yyyy) : ");
    scanf("%d/%d/%d", &month, &day, &year);
    // Enter item number: 583
    // Enter unit price: 13.5
    // Enter purchase date (mm/dd/yyyy) : 10/24/2010

    printf("\n");

    printf("Item\t\tUnit\t\tPurchase\n");
    printf("\t\tPrice\t\tDate\n");
    printf("%-d\t\t$%7.2f\t%d/%d/%d\n", item_number, unit_price, month, day, year);
    // Item            Unit            Purchase
    //                 Price           Date
    // 583             $  13.50        10/24/2010

    return 0;
}