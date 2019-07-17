/* Modify the broker.c program of Section 5.2 by making both of the following changes:

(a) Ask the user to enter the number of shares and the price per share, instead of the value of the trade.

(b) Add statements that compute the commission charged by a rival broker ($33 plus 3¢ per share for fewer than 2000 shares; $33 plus 2¢: per share for 2000 shares or more). Display the rival's commission as well as the commission charged by the original broker.
 */

#include <stdio.h>

int main() {
    float commission, value, price_per_share;
    int shares;

    printf("Enter shares of trade: ");
    scanf("%d", &shares);
    // Enter shares of trade: 3000

    printf("Enter price_per_share of trade: ");
    scanf("%f", &price_per_share);
    // Enter price_per_share of trade: 2

    value = shares * price_per_share;

    if (value < 2500.00f)
        commission = 30.00f + .017f * value;
    else if (value < 6250.00f)
        commission = 56.00f + .0066f * value;
    else if (value < 20000.00f)
        commission = 76.00f + .0034f * value;
    else if (value < 50000.00f)
        commission = 100.00f + .0022f * value;
    else if (value < 500000.00f)
        commission = 155.00f + .0011f * value;
    else
        commission = 255.00f + .0009f * value;

    if (commission < 39.00f)
        commission = 39.00f;

    printf("Commission of original broker: $%.2f\n", commission);
    // Commission of original broker: $95.60

    if (shares < 2000)
        commission = 33.00f + .03f * shares;
    else
        commission = 33.00f + .02f * shares;

    printf("Commission of rival broker: $%.2f\n", commission);
    // Commission of rival broker: $93.00

    return 0;
}
