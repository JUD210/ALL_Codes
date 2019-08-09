/*********************************************************
 * From C PROGRAMMING: A MODERN APPROACH, Second Edition *
 * By K. N. King                                         *
 * Copyright (c) 2008, 1996 W. W. Norton & Company, Inc. *
 * All rights reserved.                                  *
 * This program may be freely distributed for class use, *
 * provided that this copyright notice is retained.      *
 *********************************************************/

/* deal.c (Chapter 8, page 173) */
/* Deals a random hand of cards */

/* To pick cards randomly, we'll use several C library functions.

- The time function (from <time.h>) returns the current time, encoded in a single number.
- The srand function (from <stdlib.h>) initializes C's random number generator. Passing the return value of time to srand prevents the program from dealing the same cards every time we run it.
- The rand function (also from <stdlib.h>) produces an apparently random number each time it's called. By using the % operator, we can scale the return value from rand so that it falls between 0 and 3 (for suits) or between 0 and 12 (for ranks).
 */

#include <stdbool.h> /* C99 only */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM_SUITS 4
#define NUM_RANKS 13

int main() {
    bool in_hand[NUM_SUITS][NUM_RANKS] = {false};
    // Even though in_hand is a two-dimensional array, we can use a single pair of braces (at the risk of possibly incurring a warning from the compiler). Also, we've supplied only one value in the initializer, knowing that the compiler will fill in 0 (false) for the other elements.

    int num_cards, rank, suit;
    const char rank_code[] = {'2', '3', '4', '5', '6', '7', '8',
                              '9', 't', 'j', 'q', 'k', 'a'};
    // 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace
    const char suit_code[] = {'c', 'd', 'h', 's'};
    // Clubs, Diamond, Hearts, Spades

    srand((unsigned)time(NULL));

    printf("Enter number of cards in hand: ");
    scanf("%d", &num_cards);

    printf("Your hand:");
    while (num_cards > 0) {
        suit = rand() % NUM_SUITS; /* picks a random suit */
        rank = rand() % NUM_RANKS; /* picks a random rank */
        if (!in_hand[suit][rank]) {
            in_hand[suit][rank] = true;
            num_cards--;
            printf(" %c%c", rank_code[rank], suit_code[suit]);
        }
    }
    printf("\n");

    return 0;
}

// Enter number of cards in hand: 5
// Your hand: 9c 2d ah 7h 3d
