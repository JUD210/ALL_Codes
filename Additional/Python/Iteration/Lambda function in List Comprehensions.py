# There is a much better solution.

print([x * x for x in range(10)])
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# But, if you want to use lambda...here it is.

print([(lambda x: x * x)(num) for num in range(10)])
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print([(lambda x: x * x)(x) for x in range(10)])
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print([lambda x: x * x for num in range(3)])
# [<function <lambda> at 0x00000000023AD438>, <function <lambda> at 0x00000000023AD4A8>, <function <lambda> at 0x00000000023AD3C8>]
print([lambda x: x * x for x in range(3)])
# [<function <lambda> at 0x00000000023AD438>, <function <lambda> at 0x00000000023AD4A8>, <function <lambda> at 0x00000000023AD3C8>]
