/* (C99) Repeat Exercise 3, but this time use a designated initializer. Make the initializer as short as possible.
 */

#include <stdbool.h>
#include <stdio.h>

int main() {
    bool weekend[] = {[0] = true, [6] = true};

    for (int i = 0; i < sizeof(weekend) / sizeof(weekend[0]); i++) {
        printf("weekend{%d}: ", i);

        if (weekend[i]) {
            printf("true\n", i);
        } else {
            printf("false\n", i);
        }
    }

    return 0;
}

// weekend{0}: true
// weekend{1}: false
// weekend{2}: false
// weekend{3}: false
// weekend{4}: false
// weekend{5}: false
// weekend{6}: true
