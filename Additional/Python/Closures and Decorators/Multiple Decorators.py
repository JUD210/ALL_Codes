# https://www.codementor.io/moyosore/a-dive-into-python-closures-and-decorators-part-2-ab2enoyjg


def hello(f):
    print(f"{f} in @hello")

    def f_wrapper(name):
        print("in wrapper of @hello")
        print(f"name:{name}, f(name):{f(name)}")
        return f"Hello {f(name)}"

    return f_wrapper


def uppercase(f):
    print(f"{f} in @uppercase")

    def f_wrapper(name):
        print("in wrapper of @uppercase")
        print(f"name:{name}, f(name):{f(name)}")
        return f(name).upper()

    return f_wrapper


def split_string(f):
    print(f"{f} in @split_string")

    def f_wrapper(name):
        print("in wrapper of @split_string")
        print(f"name:{name}, f(name):{f(name)}")
        return f(name).split()

    return f_wrapper


@hello  # first applied
def say_hello_to1(name):
    return name.upper()


@uppercase  # Second applied
@hello  # first applied
def say_hello_to2(name):
    return name.upper()


@split_string  # Third applied
@uppercase  # Second applied
@hello  # first applied
def say_hello_to3(name):
    return name.upper()


# <function say_hello_to1 at 0x000002403A363598> in @hello
# <function say_hello_to2 at 0x000002403A3636A8> in @hello
# <function hello.<locals>.f_wrapper at 0x000002403A363730> in @uppercase
# <function say_hello_to3 at 0x000002403A363840> in @hello
# <function hello.<locals>.f_wrapper at 0x000002403A3638C8> in @uppercase
# <function uppercase.<locals>.f_wrapper at 0x000002403A363950> in @split_string


print(
    f"""
=== say_hello_to1("hyuk1") @hello ===
{say_hello_to1("hyuk1")}
"""
)
# in wrapper of @hello
# name:hyuk1, f(name):HYUK1

# === say_hello_to1("hyuk1") @hello ===
# Hello HYUK1

print(
    f"""
=== say_hello_to2("hyuk2") @hello @uppercase ===
{say_hello_to2("hyuk2")}
"""
)
# in wrapper of @uppercase
# in wrapper of @hello
# name:hyuk2, f(name):HYUK2
# name:hyuk2, f(name):Hello HYUK2

# in wrapper of @hello
# name:hyuk2, f(name):HYUK2

# === say_hello_to2("hyuk2") @hello @uppercase ===
# HELLO HYUK2


print(
    f"""
=== say_hello_to3("hyuk3") @hello @uppercase @split_string ===
{say_hello_to3("hyuk3")}
"""
)

""" EXPLANATION

The say_hello_to3 function returns output
HYUK3 -- by -- return name.upper()
This output is then passed into @hello

When @hello is applied, we get returned output
Hello HYUK3 -- by -- return f"Hello {f(name)}"
This output is then passed into @uppercase

When @uppercase is applied, we get returned output
HELLO HYUK3 -- by -- return f(name).upper()
This output is then passed into @split_string

When @split_string is applied, we get returned output
['HELLO', 'HYUK3'] -- by -- return f(name).upper()
This output is final return.

"""

# in wrapper of @split_string
# in wrapper of @uppercase
# in wrapper of @hello
# name:hyuk3, f(name):HYUK3
# name:hyuk3, f(name):Hello HYUK3
# in wrapper of @hello
# name:hyuk3, f(name):HYUK3
# name:hyuk3, f(name):HELLO HYUK3

# in wrapper of @uppercase
# in wrapper of @hello
# name:hyuk3, f(name):HYUK3
# name:hyuk3, f(name):Hello HYUK3

# in wrapper of @hello
# name:hyuk3, f(name):HYUK3

# === say_hello_to3("hyuk3") @hello @uppercase @split_string ===
# ['HELLO', 'HYUK3']
