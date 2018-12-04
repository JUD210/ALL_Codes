# def cylinder_volume(radius=5, height):
#     pi = 3.14159
#     return height * pi * radius ** 2
#
# SyntaxError: non-default argument follows default argument


def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2


# Pass in arguments by position.
print(cylinder_volume(10, 3))
# 282.7431


# Pass in arguments by name.
print(cylinder_volume(height=10, radius=3))
# 282.7431
