for num in range(-3, 4):
    print("{n:2} >= 0".format(n=num)) if num >= 0 else print(str(num) + " < 0")  # type: ignore
# -3 < 0
# -2 < 0
# -1 < 0
#  0 >= 0
#  1 >= 0
#  2 >= 0
#  3 >= 0
