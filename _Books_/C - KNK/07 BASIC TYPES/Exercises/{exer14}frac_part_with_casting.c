/* Does the following statement always compute the fractional part of f correctly
(assuming that f and frac_part are float variables)?

frac_part = f - (int) f;

If not, what's the problem?

--------

This statement does compute the fractional part of f correctly because of
operator precendence. */

#include <stdio.h>

int main() {
    float f = 5.6;
    float frac_part;

    printf("%f", frac_part = f - (int)f);
    // 0.6

    /* Order of precendence is

    (frac_part = (5.6 - ((int)5.6)));
    Cast(3)

    (frac_part = (5.6 - 5));
    Subtraction(5)

    frac_part = 0.6;
    Assignment(15)
     */

    return 0;
}
