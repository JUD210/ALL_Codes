# https://www.hackerrank.com/challenges/validating-the-phone-number/problem


# A valid mobile number is a ten digit number starting with a  or .
# True = Yes, False = No

import re

for _ in range(int(input())):
    # 2
    s = input()
    if re.match(r"[789]\d{9}$", s):
        print("YES")
    else:
        print("NO")
# 9587456281
# 1252478965

# YES
# NO
