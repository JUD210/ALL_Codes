"""
[ Immutable, Ordered ]

ㅇUsed to store related pieces of information.
ㅇParentheses ( ) are optional, frequently omitted.
ㅇCan be indexed and sliced like a list.
"""

width, length, height = 5, 6, 7
cube = width, length, height

print(cube)
# (5, 6, 7)
print('width:{}, length:{}, height:{}'
      .format(cube[0], cube[1], cube[2]))
# width:5, length:6, height:7

x, y, z = 1, 2, 3
z, y, x = x, y, z

print(x, y, z)
# 3 2 1
