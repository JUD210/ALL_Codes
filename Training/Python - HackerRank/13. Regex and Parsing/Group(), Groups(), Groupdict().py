# https://www.hackerrank.com/challenges/re-group-groups/problem


#   m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
#
#   print(m.group(0))
#   # 'username@hackerrank.com'
#
#   print(m.group(1))
#   # 'username'
#   print(m.group(2))
#   # 'hackerrank'
#   print(m.group(3))
#   # 'com'
#
#   print(m.group(1,2,3))
#   # ('username', 'hackerrank', 'com')
#
#   #####
#
#   m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
#   print(m.groups())
#   # ('username', 'hackerrank', 'com')
#
#   #####
#
#   m = re.match(
#       r"(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)", "myname@hackerrank.com"
#   )
#   print(m.groupdict())
#   # {'user': 'myname', 'website': 'hackerrank', 'extension': 'com'}


import re

s = input()
# ..1234567891011121314151617aaa20212223

m = re.search(r"(\w(?!_))\1+", s)
print(m.group(1) if m else -1)
# 1
