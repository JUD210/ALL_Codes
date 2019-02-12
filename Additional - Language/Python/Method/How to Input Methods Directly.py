""" Using getattr() : Recommended """

s = {1, 2, 3, 4, 5, 6}

for _ in range(3):
    method, *args = input().split()
    getattr(s, method)(*map(int, args))
    print(s)
    # pop
    # {2, 3, 4, 5, 6}
    # remove 3
    # {2, 4, 5, 6}
    # discard 5
    # {2, 4, 6}


""" Using eval() : NOT Recommended!

eval() is very unsafe to use if there's some kind of user input since the user could inject malicious code in eval()'s parameter string.

"""

s = {1, 2, 3, 4, 5, 6}

for _ in range(3):
    eval("s.{0}({1})".format(*input().split() + [""]))
    print(s)
    # pop
    # {2, 3, 4, 5, 6}
    # remove 3
    # {2, 4, 5, 6}
    # discard 5
    # {2, 4, 6}


""" Using Dictionary : NOT Recommended!!!

Do I really wanna type all the methods in the code?
It's ridiculous!

It's just for practice ONLY.

"""

s = {1, 2, 3, 4, 5, 6}

methods = {"pop": s.pop, "remove": s.remove, "discard": s.discard}

for _ in range(3):
    method, *args = input().split()
    methods[method](*map(int, args))
    print(s)
    # pop
    # {2, 3, 4, 5, 6}
    # remove 3
    # {2, 4, 5, 6}
    # discard 5
    # {2, 4, 6}
