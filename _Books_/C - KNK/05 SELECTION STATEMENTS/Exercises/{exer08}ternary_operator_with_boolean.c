/* The following if statement is unnecessarily complicated. Simplify it as much as possible.

Hint: The entire statement can be replaced by a single assignment.

if (age >= 13)
  if (age <= 19)
    teenager = true;
  else
    teenager = false;
else if (age < 13)
  teenager = false;

 */

#include <stdio.h>

#define bool int
#define true 1
#define false 0

int main() {
    int age;
    bool teenager;

    age = 15;

    /*
  if (age >= 13)
    if (age <= 19)
      teenager = true;
    else
      teenager = false;
  else if (age < 13)
    teenager = false;
   */
    teenager = age >= 13 && age <= 19 ? true : false;

    printf("Age: %d\n", age);
    // Age: 15
    printf("Teenager: %s", teenager ? "true" : "false");
    // Teenager: true

    return 0;
}