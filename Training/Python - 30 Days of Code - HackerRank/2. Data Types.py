# https://www.hackerrank.com/challenges/30-data-types/problem


# Inputs
standard_input = """12
4.0
is the best place to learn and practice coding!"""


i = 4
d = 4.0
s = "HackerRank "

""" Declare second integer, double, and String variables. """
input_i = int(input())
input_d = float(input())
input_s = input()
# 12
# 4.0
# is the best place to learn and practice coding!

""" Read and save an integer, double, and String to your variables. """
sum_i = i + input_i
sum_d = d + input_d

""" Print the sum of both integer variables on a new line. """
print(sum_i)
# 16

""" Print the sum of the double variables on a new line. """
print(sum_d)
# 8.0

""" Concatenate and print the String variables on a new line
The 's' variable above should be printed first. """
print(s + input_s)
# HackerRank is the best place to learn and practice coding!
