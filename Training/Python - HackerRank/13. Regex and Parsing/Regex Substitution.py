# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem


##### Tasks

# && → and
# || → or
# Both && and || should have a space " " on both sides.


import re


def converter(match):
    if match.group(0) == "&&":
        return "and"
    elif match.group(0) == "||":
        return "or"


for _ in range(int(input())):
    print(re.sub(r"(?<= )(?:&&|\|\|)(?= )", converter, input()))

#   a = 1;
#   b = input();
#
#   if a + b > 0 && a - b < 0:
#       start()
#   elif a*b > 10 || a/b < 1:
#       stop()
#   print set(list(a)) | set(list(b))

#   Note: do not change &&& or ||| or & or |
#   #Only change those '&&' which have space on both sides.
#   #Only change those '|| which have space on both sides.

#   ↓

#   a = 1;
#   b = input();
#
#   if a + b > 0 and a - b < 0:
#       start()
#   elif a*b > 10 or a/b < 1:
#       stop()
#   print set(list(a)) | set(list(b))

#   Note: do not change &&& or ||| or & or |
#   #Only change those '&&' which have space on both sides.
#   #Only change those '|| which have space on both sides.
