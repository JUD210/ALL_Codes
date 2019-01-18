# https://realpython.com/python-f-strings/#option-2-strformat


adventages = ["faster", "easy to read"]
print(
    f"f-strings are {adventages[0]} and {adventages[1]}\n"
    f"than both %-formatting and str.format().\n"
    f'It\'s available from "Python {3+0.6}"'
)
# f-strings are faster and easy to read
# than both %-formatting and str.format().
# It's available from "Python 3.6"


message = f"""
Y    f-strings are {adventages[0]} and {adventages[1]}
E    than both %-formatting and str.format().
S    It\'s available from "Python {3+0.6}"
"""
print(message)
# Y    f-strings are faster and easy to read
# E    than both %-formatting and str.format().
# S    It's available from "Python 3.6"


f"YES!!"

######################
