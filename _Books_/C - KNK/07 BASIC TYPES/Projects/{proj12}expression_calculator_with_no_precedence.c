/* Write a program that evaluates an expression:
Enter an expression:   1+ 2.5 * 3 +100    (input)
Value of expression: 110.5

The operands in the expression are floating-point numbers; the operators are +, -, *, and /.

The expression is evaluated from left to right (no operator takes precedence over any other operator).
 */

#include <stdio.h>

int main() {
    float op1, op2;
    // op1 becomes result in the end.
    char oper,
        ch;

    printf("Enter an expression: ");
    scanf(" %f", &op1);
    /*  Entered expression has below form:
        op1 oper op2 oper op2 oper op2 ...
     */

    while ((ch = getchar()) != '\n') {
        if (ch != ' ') {  // Skip whitespace
            oper = ch;
            scanf(" %f", &op2);

            switch (oper) {
                case '+':
                    op1 += op2;
                    break;
                case '-':
                    op1 -= op2;
                    break;
                case '*':
                    op1 *= op2;
                    break;
                case '/':
                    op1 /= op2;
                    break;
            }
        }
    }

    printf("Value of expression: %.2f", op1);

    return 0;
}

// Enter an expression:   1+ 2.5 * 3 +100
// Value of expression: 110.50
