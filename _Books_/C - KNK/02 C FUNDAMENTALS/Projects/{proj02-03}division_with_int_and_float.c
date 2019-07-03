/* proj2

Write a program that computes the volume of a sphere with a 10-meter radius, using the formula  v = 4/3 * π * r^3.

Write the fraction 4/3 as 4.0f/3.0f.
(Try writing it as 4/3. What happens?)

Hint: C doesn't have an exponentiation operator, so you'll need to multiply r by itself twice to compute r^3.

////////////////////////////////////////////////////////////

   proj3

Modify the program of Programming Project 2 so that it prompts the user to enter the radius of the sphere.

*/

#include <stdio.h>

#define M_PI 3.14159265358979323846

int main()
{
  // v = 4/3 * π * r^3

  int radius;
  printf("Enter radius of sphere: ");
  scanf("%d", &radius);
  // Enter radius of sphere: 10

  float volume;

  volume = 4.0f / 3.0f * M_PI * radius * radius * radius;
  printf("The volume of a sphere with a %d-meter radius:\n %f (4.0f / 3.0f == %f)\n\n", radius, volume, 4.0f / 3.0f);
  // The volume of a sphere with a 10-meter radius:
  //  4188.790527 (4.0f / 3.0f == 1.333333)

  volume = 4.0 / 3.0f * M_PI * radius * radius * radius;
  printf("The volume of a sphere with a %d-meter radius:\n %f (4.0 / 3.0f == %f)\n\n", radius, volume, 4.0 / 3.0f);
  // The volume of a sphere with a 10-meter radius:
  //  4188.790039 (4.0 / 3.0f == 1.333333)

  volume = 4 / 3.0f * M_PI * radius * radius * radius;
  printf("The volume of a sphere with a %d-meter radius:\n %f (4 / 3.0f == %f)\n\n", radius, volume, 4 / 3.0f);
  // The volume of a sphere with a 10-meter radius:
  //  3141.790527 (4 / 3.0f == 1.333333)

  volume = 4.0f / 3.0 * M_PI * radius * radius * radius;
  printf("The volume of a sphere with a %d-meter radius:\n %f (4.0f / 3.0 == %f)\n\n", radius, volume, 4.0f / 3.0);
  // The volume of a sphere with a 10-meter radius:
  //  4188.790039 (4.0f / 3.0 == 1.333333)

  volume = 4.0f / 3 * M_PI * radius * radius * radius;
  printf("The volume of a sphere with a %d-meter radius:\n %f (4.0f / 3 == %f)\n\n", radius, volume, 4.0f / 3);
  // The volume of a sphere with a 10-meter radius:
  //  3141.790527 (4.0f / 3 == 1.333333)

  volume = 4.0 / 3.0 * M_PI * radius * radius * radius;
  printf("The volume of a sphere with a %d-meter radius:\n %f (4.0 / 3.0 == %f)\n\n", radius, volume, 4.0 / 3.0);
  // The volume of a sphere with a 10-meter radius:
  //  4188.790039 (4.0 / 3.0 == 1.333333)

  volume = 4 / 3 * M_PI * radius * radius * radius;
  printf("The volume of a sphere with a %d-meter radius:\n %f (4 / 3 == %f)\n\n", radius, volume, 4 / 3);
  // The volume of a sphere with a 10-meter radius:
  //  3141.592773 (4 / 3 == 0.000000)

  return 0;
}
