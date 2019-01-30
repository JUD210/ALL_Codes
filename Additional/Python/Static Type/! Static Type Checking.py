# https://medium.com/@ageitgey/learn-how-to-use-static-type-checking-in-python-3-6-in-10-minutes-12c86d72677b (ENGLISH)
# https://m.blog.naver.com/PostView.nhn?blogId=passion053&logNo=221070020739&proxyReferer=https%3A%2F%2Fwww.google.com%2F (KOREAN)


""" Case 1: Before """


def get_first_name(full_name):
    return full_name.split(" ")[0]


fallback_name = {"first_name": "UserFirstName", "last_name": "UserLastName"}
first_name = get_first_name(input("Please enter your name: "))

if not first_name:
    first_name = get_first_name(fallback_name)

print(f"Hi, {first_name}!")
# If an user execute this file and didn't type anything in,
# this error occurs.
#
# AttributeError: 'dict' object has no attribute 'split'
#
# This bug is not easy to be found
# if
# - Your project is huge
# - You don't have enough unit test case sample


############################################################


""" Case 2: After """

# I only changed this line
def get_first_name2(full_name2: str) -> str:
    return full_name2.split(" ")[0]


fallback_name2 = {"first_name": "UserFirstName", "last_name": "UserLastName"}
first_name2 = get_first_name2(input("Please enter your name: "))

if not first_name2:
    first_name2 = get_first_name2(fallback_name2)  # type: ignore
# "type: ignore" disables mypy in a single line.
# I typed this to prevent mypy's error message on this file.


# By declaring str type above and enabling mypy linter,
# this error occurs before run.
#
# [mypy] Argument 1 to "get_first_name2" has incompatible type "Dict[str, str]"; expected "str" [error]


print(f"Hi, {first_name2}!")


############################################################

""" Case 3: Using typing module (Verbose) """

from typing import Dict


def get_first_name3(full_name3: str) -> str:
    return full_name3.split(" ")[0]


fallback_name3: Dict[str, str] = {
    "first_name": "UserFirstName",
    "last_name": "UserLastName",
}
first_name3 = get_first_name3(input("Please enter your name: "))

if not first_name3:
    first_name3 = get_first_name3(fallback_name3)  # type: ignore
# "type: ignore" disables mypy in a single line.
# I typed this to prevent mypy's error message on this file.

print(f"Hi, {first_name3}!")
