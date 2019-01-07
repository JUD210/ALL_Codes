# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem


from collections import namedtuple

""" Using Positional Arguments

point = namedtuple("point", "x, y")
# == namedtuple("point", "x       y")

pt1 = point(1, 2)
pt2 = point(3, 4)
dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y)
# == dot_product = (pt1.x * pt2[0]) + (pt1.y * pt2[1])

print(point, pt1, pt2, dot_product, sep="\n")
# <class '__main__.point'>
# point(x=1, y=2)
# point(x=3, y=4)
# 11


    Using Keyword Arguments

car = namedtuple("car", "Price Mileage Color Class")
xyz = car(Price=100000, Mileage=30, Color="Cyan", Class="Y")

print(xyz, xyz.Mileage, sep = "\n")
# car(Price=100000, Mileage=30, Color="Cyan", Class="Y")
# 30

"""

n = int(input())
# 5

spreadsheet = namedtuple("spreadsheet", " ".join(input().split()))
# ID         MARKS      NAME       CLASS
# (order is random)


spreadsheets = list()
for i in range(n):
    spreadsheets.append(spreadsheet(*map(str, input().split())))
    # 1          97         Raymond    7
    # 2          50         Steven     4
    # 3          91         Adrian     9
    # 4          72         Stewart    5
    # 5          80         Peter      6


average = sum(int(sheet.MARKS) for sheet in spreadsheets) / len(spreadsheets)
print("{:.2f}".format(average))
# 78.00


"""
print(spreadsheets[0]._asdict())
# OrderedDict([('ID', '1'), ('MARKS', '97'), ('NAME', 'Raymond'), ('CLASS', '7')])

"""
