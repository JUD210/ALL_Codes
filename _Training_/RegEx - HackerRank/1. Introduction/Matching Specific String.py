# https://www.hackerrank.com/challenges/matching-specific-string/problem


import re


# Inputs
standard_input = """The hackerrank team is on a mission to flatten the world by restructuring the DNA of every company on the planet. We rank programmers based on their coding skills, helping companies source great programmers and reduce the time to hire. As a result, we are revolutionizing the way companies discover and evaluate talented engineers. The hackerrank platform is the destination for the best engineers to hone their skills and companies to find top engineers.
"""


# Task
#
# You have a test string . Your task is to match the string hackerrank. This is case sensitive.

# Note
#
# This is a regex only challenge. You are not required to write code.
# You only have to fill in the regex pattern in the blank (_________).


Regex_Pattern = r"hackerrank"  # Do not delete 'r'.


Test_String = input()
# The hackerrank team is on a mission to flatten the world by restructuring the DNA of every company on the planet. We rank programmers based on their coding skills, helping companies source great programmers and reduce the time to hire. As a result, we are revolutionizing the way companies discover and evaluate talented engineers. The hackerrank platform is the destination for the best engineers to hone their skills and companies to find top engineers.

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
# Number of matches : 2
