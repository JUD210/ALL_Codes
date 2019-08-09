// Modify Programming Project 7 so that it prompts for five quiz grades for each of five students, then computes the total score and average score for each student, and the average score, high score, and low score for each quiz.

#include <stdio.h>

#define NUM_STUDENTS 5
#define NUM_QUIZZES 5

int main() {
    int grades[NUM_STUDENTS][NUM_QUIZZES];

    for (int student = 0; student < NUM_STUDENTS; student++) {
        printf("Enter grades for student %d (5 digits): ", student + 1);

        for (int quiz = 0; quiz < NUM_QUIZZES; quiz++) {
            scanf("%d", &grades[student][quiz]);
        }
    }

    printf("\nStudent  Total  Average\n");
    for (int student = 0; student < NUM_STUDENTS; student++) {
        printf("%4d      ", student + 1);

        int total = 0;
        for (int quiz = 0; quiz < NUM_QUIZZES; quiz++) {
            total += grades[student][quiz];
        }

        printf("%3d     %3d\n", total, total / NUM_QUIZZES);
    }

    printf("\nQuiz  Average  High  Low\n");
    for (int quiz = 0; quiz < NUM_QUIZZES; quiz++) {
        printf("%3d     ", quiz + 1);

        int total = 0;
        int high = 0;
        int low = 100;
        for (int student = 0; student < NUM_STUDENTS; student++) {
            total += grades[student][quiz];

            if (grades[student][quiz] > high)
                high = grades[student][quiz];
            if (grades[student][quiz] < low)
                low = grades[student][quiz];
        }

        printf("%3d    %3d   %3d\n", total / NUM_STUDENTS, high, low);
    }

    return 0;
}

/*
Enter grades for student 1 (5 digits): 92 90 88 79 60
Enter grades for student 2 (5 digits): 70 64 30 89 60
Enter grades for student 3 (5 digits): 20 15 1 9 10
Enter grades for student 4 (5 digits): 100 100 100 100 100
Enter grades for student 5 (5 digits): 100 100 100 98 95

Student  Total  Average
   1      409      81
   2      313      62
   3       55      11
   4      500     100
   5      493      98

Quiz  Average  High  Low
  1      76    100    20
  2      73    100    15
  3      63    100     1
  4      75    100     9
  5      65    100    10
 */
