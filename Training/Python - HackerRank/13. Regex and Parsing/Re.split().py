# https://www.hackerrank.com/challenges/re-split/problem


import re


re_pattern = r"[,.]"

print("\n".join(re.split(re_pattern, input())))
# 100,000,000.000

# 100
# 000
# 000
# 000
