/* Write a program that f‌inds the largest in a series of numbers entered by the user. The program must prompt the user to enter numbers one by one. When the user enters 0 or a negative number, the program must display the largest nonnegative number entered:

Enter a number: 60 (input)
Enter a number: 38.3 (input)
Enter a number: 4.89 (input)
Enter a number: 100.62 (input)
Enter a number: 75.2295 (input)
Enter a number: 0 (input)

The largest number entered was 100.62

Notice that the numbers aren't necessarily integers. */

#include <stdio.h>

int main() {
    float num, max;

    max = 0;
    do {
        printf("Enter a number: ");
        scanf("%f", &num);
        // Enter a number: 60
        // Enter a number: 38.3
        // Enter a number: 4.89
        // Enter a number: 100.62
        // Enter a number: 75.2295
        // Enter a number: 0

        if (num > max)
            max = num;

    } while (num > 0);

    printf("The largest number entered was %.2f", max);
    // The largest number entered was 100.62

    return 0;
}
