/* Write a program that generates a "random walk" across a 10*10 array. The array will contain characters (all NO_TRACE initially).

The program must randomly "walk" from element to element, always going up, down, left, or right by one element.

The elements visited by the program will be labeled with the letters A through Z, in the trace visited. Here's an example of the desired output:

A . . . . . . . . .
B C D . . . . . . .
. F E . . . . . . .
H G . . . . . . . .
I . . . . . . . . .
J . . . . . . . Z .
K . . R S T U V Y .
L M P Q . . . W X .
. N O . . . . . . .
. . . . . . . . . .

Hint: Use the srand and rand functions (see deal.c to generate random numbers. After generating a number, look at its remainder when divided by 4. There are four possible values for the remainder ㅡ0, 1, 2, and 3ㅡ indicating the direction of the next move.

Before performing a move, check that
(a) it won't go outside the array, and
(b) it doesn't take us to an element that already has a letter assigned.

If either condition is violated, try moving in another direction. If all four directions are blocked, the program must terminate. Here's an example of premature termination:

A B G H I . . . . .
. C F . J K . . . .
. D E . M L . . . .
. . . . N O . . . .
. . W X Y P Q . . .
. . V U T S R . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .

Y is blocked on all four sides. so there's no place to put Z.
 */

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE_X 10
#define SIZE_Y 10
#define NO_TRACE '.'

#define NUM_DIRECTIONS 4
#define LEFT 0
#define RIGHT 1
#define UP 2
#define DOWN 3

int main() {
    char map[SIZE_Y][SIZE_X];
    char coord_x = 0, coord_y = 0;  // current location (coordinate)

    // Initializes C's random number generator.
    srand((unsigned)time(NULL));

    // Initializes map
    for (int y = 0; y < SIZE_Y; y++) {
        for (int x = 0; x < SIZE_X; x++) {
            map[y][x] = NO_TRACE;
        }
    }

    // Move on 4 directions
    // Moving path: A -> B -> C -> ... -> Y -> Z
    for (char trace = 'A'; trace <= 'Z'; trace++) {
        map[coord_y][coord_x] = trace;

        bool is_movable[4] = {false};
        int movable_directions_count = 0;

        // Check movable directions
        if (coord_x - 1 >= 0 && map[coord_y][coord_x - 1] == NO_TRACE) {
            is_movable[LEFT] = true;
            movable_directions_count++;
        }
        if (coord_x + 1 <= SIZE_X && map[coord_y][coord_x + 1] == NO_TRACE) {
            is_movable[RIGHT] = true;
            movable_directions_count++;
        }
        if (coord_y - 1 >= 0 && map[coord_y - 1][coord_x] == NO_TRACE) {
            is_movable[UP] = true;
            movable_directions_count++;
        }
        if (coord_y + 1 <= SIZE_Y && map[coord_y + 1][coord_x] == NO_TRACE) {
            is_movable[DOWN] = true;
            movable_directions_count++;
        }

        // Terminate program if there is no movable direction.
        if (movable_directions_count == 0) {
            printf("All four sides are blocked! program terminated.\n\n");
            break;
        }

        // Perform a move.
        while (true) {
            int direction = rand() % NUM_DIRECTIONS;

            if (is_movable[direction]) {
                switch (direction) {
                    case LEFT:
                        coord_x -= 1;
                        break;
                    case RIGHT:
                        coord_x += 1;
                        break;
                    case UP:
                        coord_y -= 1;
                        break;
                    case DOWN:
                        coord_y += 1;
                        break;
                }
                break;  // The move was performed.
            } else {
                continue;  // The direction wasn't movable.
            }
        }
    }

    // Draw results
    for (int y = 0; y < SIZE_Y; y++) {
        for (int x = 0; x < SIZE_X; x++) {
            printf("%c ", map[y][x]);
        }
        printf("\n");
    }

    return 0;
}

// A D E . . . . . . .
// B C F G . . . . . .
// . . I H . . . . . .
// . . J K . . . . . .
// . Z . L M . . . . .
// X Y P O N . . . . .
// W . Q . . . . . . .
// V S R . . . . . . .
// U T . . . . . . . .
// . . . . . . . . . .

// All four sides are blocked! program terminated.
//
// A H G F . . . . . .
// B C D E . . . . . .
// . . . . . . . . . .
// . . . . . . . . . .
// . . . . . . . . . .
// . . . . . . . . . .
// . . . . . . . . . .
// . . . . . . . . . .
// . . . . . . . . . .
// . . . . . . . . . .
