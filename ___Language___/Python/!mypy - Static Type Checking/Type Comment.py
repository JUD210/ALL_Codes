def test(x):
    # type: (int) -> int
    return x + 100


print(test("3"))  # type: ignore
# [mypy] Argument 1 to "test" has incompatible type "str"; expected "int" [error]


# fmt: off
def headline(
    text,           # type: str
    width=80,       # type: int
    fill_char="-",  # type: str
):                  # type: (...) -> str
    return f" {text.title()} ".center(width, fill_char)
# fmt: on


print(headline("type comments work", width="40"))  # type: ignore
# Before running
#
# [mypy] Argument "width" to "headline" has incompatible type "str"; expected "int" [error]

# After running
#
# TypeError: 'str' object cannot be interpreted as an integer
