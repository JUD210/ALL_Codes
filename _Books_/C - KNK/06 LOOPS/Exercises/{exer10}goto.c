/* Show how to replace a continue statement by an equivalent goto statement. */

#include <stdio.h>

int main() {
    int i;

    for (i = 0; i < 5; i++) {
        if (i % 2)
            continue;
        printf("%d ", i);
    }
    // 0 2 4

    printf("\n");

    for (i = 0; i < 5; i++) {
        if (i % 2)
            goto loop_end;
        printf("%d ", i);

    loop_end:; /* null statement */
    }
    // 0 2 4

    return 0;
}