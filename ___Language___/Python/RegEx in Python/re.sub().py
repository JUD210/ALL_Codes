# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem


import re

##### Transformation of Strings

# Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number ** 2)


print(re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9"))
# 1 4 9 16 25 36 49 64 81


##### Replacements in Strings ###

html = """
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie"  value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
"""

# remove comment
print(re.sub("(<!--.*?-->)", "", html))

# <head>
# <title>HTML</title>
# </head>
# <object type="application/x-flash"
#   data="your-file.swf"
#   width="0" height="0">
#
#   <param name="quality" value="high"/>
# </object>
