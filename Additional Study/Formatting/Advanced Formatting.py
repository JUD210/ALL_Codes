# https://pyformat.info


""" Basic Formatting """
print("{} {} {}".format(1, "two", 3))
# 1 two 3

print("{2} {0} {1}".format(1, "two", 3))
# 3 1 two


""" Value Conversion """


class Data(object):
    def __str__(self):
        return "str"

    def __repr__(self):
        return "r★pr"


print("{0!s} {0!r} {0!a}".format(Data()))
# str r★pr r\u2605pr


""" Padding and aligning strings """
print("~" + "{:<10}".format("test") + "~")
print("~" + "{:10}".format("test") + "~")
# ~test      ~
# ~test      ~

print("~" + "{:>10}".format("test") + "~")
# ~      test~

print("~" + "{:_<10}".format("test") + "~")
# ~test______~
print("~" + "{:_>10}".format("test") + "~")
# ~______test~

print("~" + "{:^10}".format("test") + "~")
# ~   test   ~

print("~" + "{:^10}".format("zip") + "~")
# ~   zip    ~


""" Truncating long strings """
print("~" + "{:.10}".format("00112233445566778899") + "~")
# ~001123344~


""" Combining truncating and padding """
print("~" + "{:20.10}".format("00112233445566778899") + "~")
# ~0011223344          ~


""" Numbers """
# Decimal
print("{:d}".format(100))
# 100

# Floating Point Decimal
print("{:f}".format(3.141592653589793))
# 3.141593

# Octal
print("{:o}".format(100))
# 12

# Hexadecimal (lowercase)
print("{:x}".format(10))
# a

# Hexadecimal (uppercase)
print("{:X}".format(10))
# A

# Binary
print("{:b}".format(100))
# 1100100


""" Padding numbers """
print("~" + "{:4d}".format(42) + "~")
# ~  42~

print("{:04d}".format(42))
# 0042


print("{:01.2f}".format(31.41592653589793))
# 31.42

print("{:07.2f}".format(31.41592653589793))
# 0031.42


print("{:020}".format(31.41592653589793))
# 00031.41592653589793

print("{:07}".format(31.41592653589793))
# 31.41592653589793


print("{:.2}".format(31.41592653589793))
# 3.1e+01

print("{:.4}".format(31.41592653589793))
# 31.42


print("{:.3f}".format(31.41592653589793))
# 31.416


""" Signed numbers """
print("{:+d}".format(42))
# +42
print("{: d}".format(-23))
# -23
print("{: d}".format(42))
#  42
print("{:=+5d}".format(23))
# +  23


""" Named Placeholders """
data = {"first": "n0", "middle": "n5", "last": "n9"}

print("{first} {last}".format(**data))
# n0 n9

print("{} {}".format(data.get("first"), data.get("last")))
# n0 n9

print("{first} {last}".format(last="last", first="first"))
# first last


""" Getitem and Getattr """
person = {"first": "Jean-Luc", "last": "Picard"}
print("{p[first]} {p[last]}".format(p=person))
# Jean-Luc Picard


data = [4, 8, 15, 16, 23, 42]
print("{d[4]} {d[5]}".format(d=data))
# 23 42


class Plant(object):
    type = "tree"
    kinds = [{"name": "oak"}, {"name": "maple"}]


print("{p.type}: {p.kinds[0][name]}".format(p=Plant()))
# tree: oak


""" Datetime """
from datetime import datetime

print("{:%Y-%m-%d %H:%M}".format(datetime(2001, 2, 3, 4, 5)))
# 2001-02-03 04:05

print("{:%Y-%m-%d %H:%M}".format(datetime.now()))
# 2018-12-07 09:04

print(datetime.now())
# 2018-12-07 09:04:52.540593


""" Parametrized formats """
print("~" + "{:{align}{width}}".format("test", align="^", width="10") + "~")
# ~   test   ~

print("~" + "{:.{prec}} = {:.{prec}f}".format("Gibberish", 2.7182, prec=3) + "~")
# ~Gib = 2.718~

print("~" + "{:{width}.{prec}f}".format(2.7182, width=5, prec=2) + "~")
# ~ 2.72~

print("{:{prec}} = {:{prec}}".format("Gibberish", 2.7182, prec=".3"))
# Gib = 2.72


dt = datetime(2001, 2, 3, 4, 5)
print("{:{dfmt} {tfmt}}".format(dt, dfmt="%Y-%m-%d", tfmt="%H:%M"))
# 2001-02-03 04:05

print("~" + "{:{}{}{}.{}}".format(2.7182818284, ">", "+", 10, 3) + "~")
# ~     +2.72~

print("~" + "{:{}{sign}{}.{}}".format(2.7182818284, ">", 10, 3, sign="+") + "~")
# ~     +2.72~


""" Custom objects """


class HAL9000(object):
    def __format__(self, format):
        if format == "open-the-pod-bay-doors":
            return "I'm afraid I can't do that."
        return "HAL 9000"


print("{:open-the-pod-bay-doors}\n{:nothing}".format(HAL9000(), HAL9000()))
# I'm afraid I can't do that.
# HAL 9000
