/*********************************************************
 * From C PROGRAMMING: A MODERN APPROACH, Second Edition *
 * By K. N. King                                         *
 * Copyright (c) 2008, 1996 W. W. Norton & Company, Inc. *
 * All rights reserved.                                  *
 * This program may be freely distributed for class use, *
 * provided that this copyright notice is retained.      *
 *********************************************************/

/* checking.c (Chapter 6, page 115) */
/* Balances a checkbook */

#include <stdio.h>

int main() {
    int cmd;
    float balance = 0.0f, credit, debit;

    printf("*** ACME checkbook-balancing program ***\n");
    printf("Commands: 0=clear, 1=credit, 2=debit, ");
    printf("3=balance, 4=exit\n\n");
    // *** ACME checkbook-balancing program ***
    // Commands: 0=clear, 1=credit, 2=debit, 3=balance, 4=exit

    for (;;) {
        printf("Enter command: ");
        scanf("%d", &cmd);
        switch (cmd) {
            case 0:
                balance = 0.0f;
                break;
            case 1:
                printf("Enter amount of credit: ");
                scanf("%f", &credit);
                balance += credit;
                break;
            case 2:
                printf("Enter amount of debit: ");
                scanf("%f", &debit);
                balance -= debit;
                break;
            case 3:
                printf("Current balance: $%.2f\n", balance);
                break;
            case 4:
                return 0;
            default:
                printf("Commands: 0=clear, 1=credit, 2=debit, ");
                printf("3=balance, 4=exit\n\n");
                break;
        }
    }
    // Enter command: 3
    // Current balance: $0.00
    // Enter command: 1
    // Enter amount of credit: 10.52
    // Enter command: 2
    // Enter amount of debit: .52
    // Enter command: 3
    // Current balance: $10.00
    // Enter command: 0
    // Enter command: 3
    // Current balance: $0.00
    // Enter command: 4
}
