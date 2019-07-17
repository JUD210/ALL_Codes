/* Translate the for statement of Exercise 8 into an equivalent while statement.

for (int i = 10; i >= 1; i /= 2)
  printf("%d ", i++);
// 10 5 3 2 1 1 1 1 1 1 ...

You will need one statement in additinn to the while loop itself. */

#include <stdio.h>

int main() {
    int i = 10;
    while (i >= 1) {
        printf("%d ", i++);
        i /= 2;
    }
    // 10 5 3 2 1 1 1 1 1 1 ...

    return 0;
}