# https://medium.com/understand-the-python/understanding-the-asterisk-of-python-8b9daaa4a558


# Initialize the zero-valued list with 10 length
zeros_list = [0] * 10
print(zeros_list)
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# Declare the zero-valued tuple with 10 length
zeros_tuple = (0,) * 10
print(zeros_tuple)
# (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


# Extending the "vector_list" by 3 times
vector_list = [[1, 2, 3]]
for i, vector in enumerate(vector_list * 3):
    print("{0} scalar product of vector: {1}".format((i + 1), [(i + 1) * e for e in vector]))
# 1 scalar product of vector: [1, 2, 3]
# 2 scalar product of vector: [2, 4, 6]
# 3 scalar product of vector: [3, 6, 9]