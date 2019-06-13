/* In the dweight.c program, which spaces are essential? */

#include <stdio.h>

int main()
{
  int height, length, width, volume, weight;

  height = 8;
  length = 12;
  width = 10;
  volume = height * length * width;
  weight = (volume + 165) / 166;

  printf("Dimensions: %dx%dx%d\n", length, width, height);
  printf("Volume (cubic inches): %d\n", volume);
  printf("Dimensional weight (pounds): %d\n", weight);

  return 0;
}

/* 

Dimensions: 12x10x8
Volume (cubic inches): 960
Dimensional weight (pounds): 6

 */

/* Spaces 
inside a string literal, 
between type specifier and identifier.

 */