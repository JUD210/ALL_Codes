""" Quiz: Using Truth Values of Objects

The code below is the solution to the Which Prize quiz you've seen previously. You're going to rewrite this based on what you've learned about truth values.

points = 174

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result)


You will use a new variable prize to store a prize name if one was won, and then use the truth value of this variable to compose the result message. This will involve two if statements.


1st conditional statement: update prize to the correct prize name based on points.

2nd conditional statement: set result to the correct phrase based on whether prize is evaluated as True or False.


- If prize is None, result should be set to "Oh dear, no prize this time."

- If prize contains a prize name, result should be set to "Congratulations! You won a {}!".format(prize). This will avoid having the multiple result assignments for different prizes.

At the beginning of your code, set prize to None, as the default value. 
"""


points = 174  # use this as input for your submission

# establish the default prize value to None
prize = None

# use the points value to assign prizes to the correct prize names
if points <= 50:
    prize = "wooden rabbit"
elif points <= 150:
    prize = None
elif points <= 180:
    prize = "wafer-thin mint"
else:
    prize = "penguin"

# use the truth value of prize to assign result to the correct prize
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

print(result)
