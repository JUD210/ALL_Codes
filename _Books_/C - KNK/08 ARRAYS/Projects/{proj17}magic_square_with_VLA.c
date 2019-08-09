/* Write a program that prints an n*n magic square (a square arrangement of the numbers 1, 2, ..., n^2 in which the sums of the rows, columns, and diagonals are all the same).

The user will specify the value of n:

This program creates a magic square of a specified size.
The size must be an odd number between 1 and 99.
Enter size of magic square: 5 (input)

 17 24  1  8 15
 23  5  7 14 16
  4  6 13 20 22
 10 12 19 21  3
 11 18 25  2  9

Store the magic square in a two-dimensional array. Start by placing the number 1 in the middle of row 0.

Place each of the remaining numbers 2, 3, ..., n^2 by moving up one row and over one column. Any attempt to go outside the bounds of the array should "wrap around" to the opposite side of the array.

For example, instead of storing the next number in row -1, we would store it in row n-1 (the last row). Instead of storing the next number in column n, we would store it in column 0.

If a particular array element is already occupied, put the number directly below the previously stored number.

If your compiler supports variable-length arrays, declare the array to have n rows and n columns. If not, declare the array to have 99 rows and 99 columns.
 */

#include <stdio.h>

int main() {
    int size, cur_row, cur_col;
    printf("This program creates a magic square of a specified size.\n");
    printf("The size must be an 'odd' number between '1 and 99'.\n");
    printf("Enter size of magic square: ");
    scanf("%d", &size);

    // variable-length array(VLA) in C99
    int magic_square[size][size];

    // Initialize the magic square
    for (int r = 0; r < size; r++) {
        for (int c = 0; c < size; c++) {
            magic_square[r][c] = 0;
        }
    }

    // Store the magic square in a two-dimensional array. Start by placing the number 1 in the middle of row 0.
    cur_row = 0;
    cur_col = size / 2;
    for (int n = 1; n <= size * size; n++) {
        magic_square[cur_row][cur_col] = n;

        // Move up one row and over one column.
        int row = cur_row - 1;
        int col = cur_col + 1;

        // Any attempt to go outside the bounds of the array should "wrap around" to the opposite side of the array.
        if (row == -1) {
            row = size - 1;
        }
        if (col == size) {
            col = 0;
        }

        // If a particular array element is already occupied, put the number directly below the previously stored number.
        if (magic_square[row][col]) {
            cur_row += 1;

            // Any attempt to go outside the bounds of the array should "wrap around" to the opposite side of the array.
            if (cur_row == size) {
                cur_row = 0;
            }
        } else {
            cur_row = row;
            cur_col = col;
        }
    }

    // Prints the magic square
    for (int r = 0; r < size; r++) {
        for (int c = 0; c < size; c++) {
            printf("%5d", magic_square[r][c]);
        }
        printf("\n");
    }

    return 0;
}

// This program creates a magic square of a specified size.
// The size must be an 'odd' number between '1 and 99'.
// Enter size of magic square: 5
//    17   24    1    8   15
//    23    5    7   14   16
//     4    6   13   20   22
//    10   12   19   21    3
//    11   18   25    2    9
