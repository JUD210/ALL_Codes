/* Write a declaration of an array named weekend containing seven bool values. Include an initializer that makes the first and last values true; all other values should be false.
 */

#include <stdbool.h>
#include <stdio.h>

int main() {
    bool weekend[] = {true, false, false, false, false, false, true};

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
