# https://www.hackerrank.com/challenges/validate-a-roman-number/problem


# num constraint : 1~3999

# | character | numerical value |
# | --------- | --------------- |
# | I         | 1               |
# | V         | 5               |
# | X         | 10              |
# | L         | 50              |
# | C         | 100             |
# | D         | 500             |
# | M         | 1000            |

# | --------------------------------------- |
# | 1   | I    | 11  | XI    | 21  | XXI    |
# | 2   | II   | 12  | XII   | 22  | XXII   |
# | 3   | III  | 13  | XIII  | 23  | XXIII  |
# | 4   | IV   | 14  | XIV   | 24  | XXIV   |
# | 5   | V    | 15  | XV    | 25  | XXV    |
# | 6   | VI   | 16  | XVI   | 26  | XXVI   |
# | 7   | VII  | 17  | XVII  | 27  | XXVII  |
# | 8   | VIII | 18  | XVIII | 28  | XXVIII |
# | 9   | IX   | 19  | XIX   | 29  | XXIX   |
# | 10  | X    | 20  | XX    | 30  | XXX    |

# fmt:off
import re

IVX = r"(?:V?I{0,3}|I[XV])"  # 1, 2, ... 9
XLC = r"(?:L?X{0,3}|X[CL])"  # 10, 20, ...90
CDM = r"(?:D?C{0,3}|C[MD])"  # 100, 200, ... 900
M__ = r"(?:M{0,3})"          # 1000, 2000, 3000

regex_pattern = rf"{M__}{CDM}{XLC}{IVX}$"
# "$" is essential because of a case like "DXXVIIII" (False)

while True:
    print(str(bool(re.match(regex_pattern, input()))))
# DCCCLXX   ### 500 + 100*3 + 50 + 10*2

# True
