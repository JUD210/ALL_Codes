""" For Loops Vs. While Loops
Now that you are familiar with both for and while loops, let's consider when it's most helpful to use each of them.
"""


""" for loops are ideal when the number of iterations is known or finite.

Examples:

When you have an iterable collection (list, string, set, tuple, dictionary)
    for name in names:

When you want to iterate through a loop for a definite number of times, using range()
    for i in range(5):

"""

""" while loops are ideal when the iterations need to continue until a condition is met.

Examples:

When you want to use comparison operators
    while count <= 100:

When you want to loop based on receiving specific user input.
    while user_input == 'y':

"""

# Please use this space to test and run your code

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542,
            87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
odd_num_list = []

for num in num_list:
    if num % 2 == 1:
        odd_num_list.append(num)

print(odd_num_list)

odd_count = 0
while len(odd_num_list) > 0 and odd_count < 5:
    print(odd_num_list.pop(0))
    odd_count += 1


""" [Solution] """

# num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542,
#             87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
            
# count_odd = 0
# list_sum = 0
# i = 0
# len_num_list = len(num_list)

# while (count_odd < 5) and (i < len_num_list):
#     if num_list[i] % 2 != 0:
#         list_sum += num_list[i]
#         count_odd += 1
#     i += 1

# print("The numbers of odd numbers added are: {}".format(count_odd))
# print("The sum of the odd numbers added is: {}".format(list_sum))
