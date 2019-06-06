""" Quiz: Write a Docstring

Write a docstring for the readable_timedelta function you defined earlier! Remember the way you write your docstrings is pretty flexible! Look through Python's docstring conventions here and check out this Stack Overflow page for some inspiration!
"""


def readable_timedelta(days):
    """ 
    Return a string of the number of weeks and days included in days.
    
    Arguments:
        days {int} -- number of days to convert
    
    Returns:
        {str} -- "{} week(s) and {} day(s)"
    """
    # insert your docstring here

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
