# https://realpython.com/python-type-checking/


# In this tutorial, you'll learn about the following:
#
# Type annotations and type hints
# Adding static types to code, both your code and the code of others
# Running a static type checker
# Enforcing types at runtime


# So, should you use static type checking in your own code? Well, it's not an all-or-nothing question. Luckily, Python supports the concept of gradual typing. This means that you can gradually introduce types into your code. Code without type hints will be ignored by the static type checker. Therefore, you can start adding types to critical components, and continue as long as it adds value to you.


""" Case 1: Before Type Checking """


def headline(txt, align=True):
    if align:
        return f"{txt.title()}\n{'-' * len(txt)}"
    else:
        return f" {txt.title()} ".center(50, "o")


print(headline("Python type checking"))
# Python Type Checking
# --------------------
print(headline("Python type checking", align=False))
# oooooooooooooo Python Type Checking oooooooooooooo

print(headline("Python type checking", align="left"))
# Python Type Checking
# --------------------
print(headline("Python type checking", align="middle"))
# Python Type Checking
# --------------------
print(headline("Python type checking", align="right"))
# Python Type Checking
# --------------------


""" Case 2: After Type Checking """


def headline2(txt: str, align: bool = True) -> str:
    if align:
        return f"{txt.title()}\n{'-' * len(txt)}"
    else:
        return f" {txt.title()} ".center(50, "o")


print(headline2("Python type checking"))
# Python Type Checking
# --------------------
print(headline2("Python type checking", align=False))
# oooooooooooooo Python Type Checking oooooooooooooo

print(headline2("Python type checking", align="left"))  # type: ignore
# Below error occurs! but as it's the mypy linter's error, prints same result.
# [mypy] Argument "align" to "headline2" has incompatible type "str"; expected "bool" [error]
#
# Python Type Checking
# --------------------
print(headline2("Python type checking", align="middle"))  # type: ignore
# Below error occurs! but as it's the mypy linter's error, prints same result.
# [mypy] Argument "align" to "headline2" has incompatible type "str"; expected "bool" [error]
#
# Python Type Checking
# --------------------
print(headline2("Python type checking", align="right"))  # type: ignore
# Below error occurs! but as it's the mypy linter's error, prints same result.
# [mypy] Argument "align" to "headline2" has incompatible type "str"; expected "bool" [error]
#
# Python Type Checking
# --------------------


""" Case 3: Let's fix the bug! """


def headline3(txt: str, centered: bool = False) -> str:
    if centered:
        return f"{txt.title()}\n{'-' * len(txt)}"
    else:
        return f" {txt.title()} ".center(50, "o")


print(headline3("Python type checking"))
# Python Type Checking
# --------------------
print(headline3("Python type checking", centered=True))
# oooooooooooooo Python Type Checking oooooooooooooo
