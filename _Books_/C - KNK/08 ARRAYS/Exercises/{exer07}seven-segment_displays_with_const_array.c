/* Using the shortcuts described in Section 8.2, shrink the initializcr for the segments array (Exercise 6) as much as you can.
 */

#include <stdio.h>

int main() {
    const int segments[10][7] = {{1, 1, 1, 1, 1, 1},
                                 {0, 1, 1},
                                 {1, 1, 0, 1, 1, 0, 1},
                                 {1, 1, 1, 1, 0, 0, 1},
                                 {0, 1, 1, 0, 0, 1, 1},
                                 {1, 0, 1, 1, 0, 1, 1},
                                 {1, 0, 1, 1, 1, 1, 1},
                                 {1, 1, 1},
                                 {1, 1, 1, 1, 1, 1, 1},
                                 {1, 1, 1, 1, 0, 1, 1}};

    return 0;
}