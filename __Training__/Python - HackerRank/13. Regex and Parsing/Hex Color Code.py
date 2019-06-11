# https://www.hackerrank.com/challenges/hex-color-code/problem


### CSS Code Pattern

# Selector
# {
#     Property: Value;
# }


### Specifications of HEX Color Code

# ■ It must start with a '#' symbol.
# ■ It can have 3 or 6 digits.
# ■ Each digit is in the range of 0 to F. (1, 2, 3, ... A, B, ... F).
# ■ A-F letters can be lower case.

# Output the valid color codes with '#' symbols on separate lines.
# Color codes used as selectors must be excepted.


import re

for _ in range(int(input())):
    # 11

    s = input()
    # #BED
    # {
    #     color: #FfFdF8; background-color:#aef;
    #     font-size: 123px;
    #     background: -webkit-linear-gradient(top, #f9f9f9, #fff);
    # }
    # #Cab
    # {
    #     background-color: #ABC;
    #     border: 2px dashed #fff;
    # }

    m = re.findall(r"(?<!^)(#(?:[\da-fA-F]{3}){1,2})", s)
    if m:
        print("\n".join(m))
# #FfFdF8
# #aef
# #f9f9f9
# #fff
# #ABC
# #fff
