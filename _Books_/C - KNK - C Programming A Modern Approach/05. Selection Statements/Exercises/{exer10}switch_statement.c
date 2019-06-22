/* What output does the following program fragment produce? (Assume that i is an integer variable.) */

#include <stdio.h>

int main()
{
  int i;

  i = 1;
  switch (i % 3)
  {
  case 0:
    printf("zero\n");
  case 1:
    printf("one\n");
  case 2:
    printf("two\n");
  }
  // one
  // two

  return 0;
}
