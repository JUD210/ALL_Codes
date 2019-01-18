# https://www.hackerrank.com/challenges/re-start-re-end/problem


#   # These expressions return the indices of the start and end of the substring matched by the group.
#
#   m = re.search(m'\d+','a1234hh1236')
#   print(m.end())
#   # 4
#   print(m.start())
#   # 0


import re

s, sub_s = input(), input()
# aaadaa
# aa

pattern = re.compile(sub_s)
m = pattern.search(s)

if not m:
    print((-1, -1))
while m:
    print(f"({m.start()}, {m.end()-1})")
    m = pattern.search(s, m.start() + 1)
# (0, 1)
# (1, 2)
# (4, 5)
