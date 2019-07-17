/* Are the following if statements equivalent? If not, why not? */

#include <stdio.h>

int main() {
    int score;

    for (score = 0; score <= 100; score += 10) {
        printf("\n[score:%d]\n", score);

        if (score >= 90)
            printf("A");
        else if (score >= 80)
            printf("B");
        else if (score >= 70)
            printf("C");
        else if (score >= 60)
            printf("D");
        else
            printf("F");

        if (score < 60)
            printf("F");
        else if (score < 70)
            printf("D");
        else if (score < 80)
            printf("C");
        else if (score < 90)
            printf("B");
        else
            printf("A");
    }

    return 0;
}

/*
  It is equivalent as you can see above.
 */