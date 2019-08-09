/* Write a program that reads a 5*5 array of integers and then prints the row sums and the column sums:

Enter row 1: 8 3 9 0 10 (input)
Enter row 2: 3 5 17 1 1 (input)
Enter row 3: 2 8 6 23 1 (input)
Enter row 4: 15 7 3 2 9 (input)
Enter row 5: 6 14 2 6 0 (input)

Row totals: 30 27 40 36 28
Column totals: 34 37 37 32 21
 */

#include <stdio.h>

#define NUM_ROW 5
#define NUM_COLUMN 5

int main() {
    const int arr[NUM_ROW][NUM_COLUMN];
    int sum;

    for (int row = 0; row < NUM_ROW; row++) {
        printf("Enter row %d (5 digits): ", row + 1);

        for (int column = 0; column < NUM_COLUMN; column++) {
            scanf("%d", &arr[row][column]);
        }
    }

    printf("\nRow totals: ");
    for (int row = 0; row < NUM_ROW; row++) {
        sum = 0;
        for (int column = 0; column < NUM_COLUMN; column++) {
            sum += arr[row][column];
        }
        printf("%d ", sum);
    }

    printf("\nColumn totals: ");
    for (int column = 0; column < NUM_COLUMN; column++) {
        sum = 0;
        for (int row = 0; row < NUM_ROW; row++) {
            sum += arr[row][column];
        }
        printf("%d ", sum);
    }

    return 0;
}

/*
Enter row 1 (5 digits): 8 3 9 0 10
Enter row 2 (5 digits): 3 5 17 1 1
Enter row 3 (5 digits): 2 8 6 23 1
Enter row 4 (5 digits): 15 7 3 2 9
Enter row 5 (5 digits): 6 14 2 6 0

Row totals: 30 27 40 36 28
Column totals: 34 37 37 32 21
 */
