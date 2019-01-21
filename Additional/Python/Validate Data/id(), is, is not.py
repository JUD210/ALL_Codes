# https://stackoverflow.com/questions/13650293/understanding-pythons-is-operator


# The operators 'is' and 'is not' test for object identity:
# 'x is y' is true if and only if 'x' and 'y' are the same object.


# Hence, 'A is B' is the same as 'id(A) == id(B)'

####################

x = "a"
x += "bc"
y = "abc"
print(
    f"""
x:{x}, id(x):{id(x)}
y:{y}, id(y):{id(y)}
∴'x==y' is {x==y}
∴'x is y' is {x is y}
"""
)
# x:abc, id(x):2600914777960
# y:abc, id(y):2600882075272
# ∴'x==y' is True
# ∴'x is y' is False


z = "abc"
w = "abc"
print(
    f"""
z:{z}, id(z):{id(z)}
w:{w}, id(w):{id(w)}
∴'z==w' is {z==w}
∴'z is w' is {z is w}
"""
)
# z:abc, id(z):2711673566856
# w:abc, id(w):2711673566856
# ∴'z==w' is True
# ∴'z is w' is True

####################


a = 0
a += 1
b = 1
print(
    f"""
a:{a}, id(a):{id(a)}
b:{b}, id(b):{id(b)}
∴'a==b' is {a==b}
∴'a is b' is {a is b}
"""
)
# a:1, id(a):140713138905936
# b:1, id(b):140713138905936
# ∴'a==b' is True
# ∴'a is b' is True

a = False
a = not a
b = True
print(
    f"""
a:{a}, id(a):{id(a)}
b:{b}, id(b):{id(b)}
∴'a==b' is {a==b}
∴'a is b' is {a is b}
"""
)
# a:True, id(a):140713138374992
# b:True, id(b):140713138374992
# ∴'a==b' is True
# ∴'a is b' is True

a = 1000
a += 1
b = 1001
print(
    f"""
a:{a}, id(a):{id(a)}
b:{b}, id(b):{id(b)}
∴'a==b' is {a==b}
∴'a is b' is {a is b}
"""
)
# a:1001, id(a):1642355294736
# b:1001, id(b):1642351970192
# ∴'a==b' is True
# ∴'a is b' is False


x = [1, 2, 3]
y = [1, 2, 3]
z = y
print(
    f"""
x:{x}, id(x):{id(x)}
y:{y}, id(y):{id(y)}
z:{z}, id(z):{id(z)}
∴'x==y' is {x==y}
∴'y==z' is {y==z}
∴'z==x' is {z==x}
∴'x==y==z' is {x==y==z}
∴'x is y' is {x is y}
∴'y is z' is {y is z}
∴'z is x' is {z is x}
∴'x is y is z' is {x is y is z}
"""
)
# x:[1, 2, 3], id(x):1642352173704
# y:[1, 2, 3], id(y):1642352173768
# z:[1, 2, 3], id(z):1642352173768
# ∴'x==y' is True
# ∴'y==z' is True
# ∴'z==x' is True
# ∴'x==y==z' is True
# ∴'x is y' is False
# ∴'y is z' is True
# ∴'z is x' is False
# ∴'x is y is z' is False

y[0] = 5
print(
    f"""
x:{x}, id(x):{id(x)}
y:{y}, id(y):{id(y)}
z:{z}, id(z):{id(z)}
∴'x==y' is {x==y}
∴'y==z' is {y==z}
∴'z==x' is {z==x}
∴'x==y==z' is {x==y==z}
∴'x is y' is {x is y}
∴'y is z' is {y is z}
∴'z is x' is {z is x}
∴'x is y is z' is {x is y is z}
"""
)

# x:[1, 2, 3], id(x):1642352173704
# y:[5, 2, 3], id(y):1642352173768
# z:[5, 2, 3], id(z):1642352173768
# ∴'x==y' is False
# ∴'y==z' is True
# ∴'z==x' is False
# ∴'x==y==z' is False
# ∴'x is y' is False
# ∴'y is z' is True
# ∴'z is x' is False
# ∴'x is y is z' is False
