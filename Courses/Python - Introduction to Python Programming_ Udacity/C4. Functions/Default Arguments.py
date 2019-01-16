def cylinder_volume(height, radius=3):
    pi = 3.14159
    return height * pi * radius ** 2


# Using the default value.
print(cylinder_volume(10))
# 282.7431


# Overriding the default value.
print(cylinder_volume(10, 3))
# 282.7431

print(cylinder_volume(10, 5))
# 785.3975
