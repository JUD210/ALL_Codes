#include <stdio.h>
#include <string.h>

int main() {
    // If an initializer isn't large enough to fill a multidimensional array, the remaining elements are given the value 0. For example, the following initializer fills only the first three rows of m; the last two rows will contain zeros:
    int a[5][9] = {{1, 1, 1, 1, 1, 1, 1, 1, 1},
                   {1, 1, 1, 1, 1, 1, 1, 1, 1},
                   {1, 1, 1, 1, 1, 1, 1, 1, 1}};
    // 1 1 1 1 1 1 1 1 1
    // 1 1 1 1 1 1 1 1 1
    // 1 1 1 1 1 1 1 1 1
    // 0 0 0 0 0 0 0 0 0
    // 0 0 0 0 0 0 0 0 0

    // If an inner list isn't long enough to fill a row, the remaining elements in the row are initialized to 0:
    int b[5][9] = {{1, 1, 1, 1, 1, 1, 1, 1, 1},
                   {1},
                   {1, 1, 1, 1},
                   {1, 1, 1, 1, 1, 1, 1},
                   {1, 1, 1, 1, 1, 1, 1, 1}};
    // 1 1 1 1 1 1 1 1 1
    // 1 0 0 0 0 0 0 0 0
    // 1 1 1 1 0 0 0 0 0
    // 1 1 1 1 1 1 1 0 0
    // 1 1 1 1 1 1 1 1 0

    // We can even omit the inner braces:
    int c[5][9] = {1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1,
                   0, 1, 1, 1, 1, 1, 1, 1, 0,
                   1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1};
    // 1 1 1 1 1 1 1 1 1
    // 1 1 1 1 1 1 1 1 1
    // 0 1 1 1 1 1 1 1 0
    // 1 1 1 1 1 1 1 1 1
    // 1 1 1 1 1 1 1 1 1

    int arr[5][9];
    for (int i = 0; i < 3; i++) {
        switch (i) {
            case 0:
                memcpy(arr, a, sizeof(arr));
                break;
            case 1:
                memcpy(arr, b, sizeof(arr));
                break;
            case 2:
                memcpy(arr, c, sizeof(arr));
                break;
        }

        for (int y = 0; y < 5; y++) {
            for (int x = 0; x < 9; x++) {
                printf("%d ", arr[y][x]);
            }
            printf("\n");
        }
        printf("\n");
    }

    return 1;
}