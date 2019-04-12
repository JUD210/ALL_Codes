# https://www.hackerrank.com/challenges/ide-identifying-comments/problem


import re
import sys

# Inputs
standard_input = """ // my  program in C++

#include <iostream>
/** playing around in
a new programming language **/
using namespace std;

int main ()
{
  cout << "Hello World";
  cout << "I'm a C++ program"; //use cout
  return 0;
}"""

# ?s == re.S == re.DOTALL
# : Make the '.' special character match any character at all, including a newline; without this flag, '.' will match anything except a newline.

# ?m == re.M == re.MULTILINE
# : When specified, the pattern character '^' matches at the beginning of the string and at the beginning of each line (immediately following each newline); and the pattern character '$' matches at the end of the string and at the end of each line (immediately preceding each newline). By default, '^' matches only at the beginning of the string, and '$' only at the end of the string and immediately before the newline (if any) at the end of the string. Corresponds to the inline flag (?m).

pattern = r"(?s)(?m)(//.*?$|/\*.*?\*/)"
txt = sys.stdin.read()

# re.sub() for Testcase #4: others will just work with comment
print(
    "\n".join(
        re.sub(r"\n\s+", "\n", comment)
        for comment in re.findall(pattern, txt)
    )
)
