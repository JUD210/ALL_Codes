/* Modify the reverse.c program of Section 8.1 to use the expression (int)
(sizeof(a) / sizeof(a[0])) (or a macro with this value) for the array length.
 */

#include <stdio.h>

#define LEN (int)(sizeof(a) / sizeof(a[0]))

int main() {
    int a[10], i;

    printf("Enter 10 numbers: ");
    for (i = 0; i < LEN; i++)
        scanf("%d", &a[i]);

    printf("In reverse order:");
    for (i = LEN - 1; i >= 0; i--)
        printf(" %d", a[i]);

    return 0;
}

// Enter 10 numbers: 34 82 49 102 7 94 23 11 50 31
// In reverse order: 31 50 11 23 94 7 102 49 82 34
