# for char in "abc123":
#     assert not char.isdigit(), f"{char} is digit! Enter alphabet ONLY."
#     print(f"{char} is not digit")

# AssertionError: 1 is digit! Enter alphabet ONLY.


for char in "abc":
    assert not char.isdigit(), f"{char} is digit"
    print(f"{char} is not digit")

# a is not digit
# b is not digit
# c is not digit
