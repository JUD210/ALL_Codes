# https://www.hackerrank.com/challenges/30-operators/problem


# Inputs
standard_input = """12.00
20
8"""


import math
import os
import random
import re
import sys


""" Complete the solve function below. """


def get_total_cost_of_meal(meal_cost, tip_percent, tax_percent):
    meal_cost
    tip = meal_cost * (tip_percent / 100)
    tax = meal_cost * (tax_percent / 100)

    return round(meal_cost + tip + tax)


meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())
# 12.00
# 20
# 8

print(get_total_cost_of_meal(meal_cost, tip_percent, tax_percent))
# 15
