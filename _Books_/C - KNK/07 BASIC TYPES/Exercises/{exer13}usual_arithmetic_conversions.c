/* Assume that a program contains the following declarations:

char c = '\1';
short s = 2;
int i = -3;
long l = 5;
float f = 6.5f;
double d = 7.5;

Give the value and the type of each expression listed below.

(a) c * i     // 1 * -3      Value = -3      Type = int
(b) s + l     // 2 + 5       Value = 7       Type = long
(c) f / c     // 6.5 / 1     Value = 6.5     Type = float
(d) d / s     // 7.5 / 2     Value = 3.75    Type = double
(e) f - d     // 6.5 - 7.5   Value = -1.0    Type = double
(f) (int) f   //             Value = 6       Type = int
 */

#include <stdio.h>

int main() {
    char c = '\1';
    short s = 2;
    int i = -3;
    long l = 5;
    float f = 6.5f;
    double d = 7.5;

    printf("%d\n", c * i);
    // -3
    printf("%ld\n", s + l);
    // 7
    printf("%f\n", f / c);
    // 6.500000
    printf("%lf\n", d / s);
    // 3.750000
    printf("%lf\n", f - d);
    // -1.000000
    printf("%d\n", (int)f);
    // 6

    return 0;
}