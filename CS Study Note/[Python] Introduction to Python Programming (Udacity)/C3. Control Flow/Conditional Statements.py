"""
if
: An if statement must always start with an if clause, which contains the first condition that is checked. If this evaluates to True, Python runs the code indented in this if block and then skips to the rest of the code after the if statement.

elif
: elif is short for "else if." An elif clause is used to check for an additional condition if the conditions in the previous clauses in the if statement evaluate to False. As you can see in the example, you can have multiple elif blocks to handle different situations.

else
: Last is the else clause, which must come at the end of an if statement if used. This clause doesn't require a condition. The code in an else block is run if all conditions above that in the if statement evaluate to False.

"""

season = 'winter'

if season == 'spring':
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
else:
    print('unrecognized season')

# stay indoors!
