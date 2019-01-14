# https://www.hackerrank.com/challenges/ginorts/problem


# All sorted lowercase letters are ahead of uppercase letterc.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.

s = input()
# Sorting1234

lowers = ""
uppers = ""
odds = ""
evens = ""

for c in s:
    if c.islower():
        lowers += c
    elif c.isupper():
        uppers += c
    elif c.isdigit():
        if int(c) % 2 == 0:
            evens += c
        else:
            odds += c

lowers = "".join(sorted(lowers))
uppers = "".join(sorted(uppers))
odds = "".join(sorted(odds))
evens = "".join(sorted(evens))

print(lowers + uppers + odds + evens)
# ginortS1324


""" Other Solutions """
print(*sorted(input(), key=lambda c: (-ord(c) >> 5, c in "02468", c)), sep="")

print(
    *sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in "02468", c)), sep=""
)

order = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468"
print(*sorted(input(), key=order.index), sep="")

import string

print(*sorted(input(), key=(string.ascii_letters + "1357902468").index), sep="")
