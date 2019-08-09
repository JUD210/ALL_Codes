/* Modify the interest.c program of Section 8.1 so that it compounds interest monthly instead of annually. The form of the output shouldn't change: the balance should still be shown at annual intervals.
 */

#include <stdio.h>

#define NUM_RATES ((int)(sizeof(value) / sizeof(value[0])))
#define INITIAL_BALANCE 100.00

int main() {
    int low_rate, num_years;
    double value[5];

    printf("Enter interest rate: ");
    scanf("%d", &low_rate);
    printf("Enter number of years: ");
    scanf("%d", &num_years);

    printf("\nYears");
    for (int i = 0; i < NUM_RATES; i++) {
        printf("%6d%%", low_rate + i);
        value[i] = INITIAL_BALANCE;
    }
    printf("\n");

    for (int year = 1; year <= num_years; year++) {
        printf("%3d    ", year);

        for (int i = 0; i < NUM_RATES; i++) {
            for (int month = 1; month <= 12; month++) {
                value[i] += ((double)(low_rate + i) / 12) / 100.0 * value[i];
            }
            printf("%7.2f", value[i]);
        }
        printf("\n");
    }

    return 0;
}

/*
Enter interest rate: 3
Enter number of years: 10

Years     3%     4%     5%     6%     7%
  1     103.04 104.07 105.12 106.17 107.23
  2     106.18 108.31 110.49 112.72 114.98
  3     109.41 112.73 116.15 119.67 123.29
  4     112.73 117.32 122.09 127.05 132.21
  5     116.16 122.10 128.34 134.89 141.76
  6     119.69 127.07 134.90 143.20 152.01
  7     123.34 132.25 141.80 152.04 163.00
  8     127.09 137.64 149.06 161.41 174.78
  9     130.95 143.25 156.68 171.37 187.42
 10     134.94 149.08 164.70 181.94 200.97
*/