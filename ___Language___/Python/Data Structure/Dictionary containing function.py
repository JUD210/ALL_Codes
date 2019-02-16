""" Using Dictionary : NOT Recommended!!!

Do I really wanna type all the methods in the code?
It's ridiculous!

It's just for practice ONLY.

"""

methods = {
    'p' : print,
    's' : sum
}

methods['p']('aaaa')
# aaaa

print(methods['s']([5,3]))
# 8

methods['a'] = sorted
print(methods['a']([5,2,1,3]))
# [1, 2, 3, 5]