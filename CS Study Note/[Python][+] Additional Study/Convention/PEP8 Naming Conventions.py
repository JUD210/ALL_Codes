# https://www.datacamp.com/community/tutorials/pep8-tutorial-python-code


""" General Naming Conventions (PEP8)

|   Identifier   | Convention |
| -------------- | ---------- |
| Module         | lowercase  |
| Class          | CapWords   |
| Functions      | lowercase  |
| Methods        | lowercase  |
| Type variables | CapWords   |
| Constants      | UPPERCASE  |
| Package        | lowercase  |

"""

# TODO: Complete examples

long_variable = 3






""" Naming Conventions

b or a single lowercase letter;

B or a single uppercase letter;

lowercase

UPPERCASE

lower_case_with_underscores

UPPER_CASE_WITH_UNDERSCORES

CapitalizedWords
: Which is also known as CapWords, CamelCase or StudlyCaps.

mixedCase

Capitalized_Words_With_Underscores

_single_leading_underscore
: Weak "internal use" indicator. for example, from M import * does not import objects whose name starts with an underscore.

single_trailing_underscore_
: Used by convention to avoid conflicts with Python keyword, for example, Tkinter.Toplevel(master, class_='ClassName')

__double_leading_underscore
: When naming a class attribute, invokes name mangling (inside class FooBar, __boo becomes _FooBar__boo).

__double_leading_and_trailing_underscore__
: "magic" objects or attributes that live in user-controlled namespaces. For example, __init__, __import__ or __file__. You should never invent such names, but only use them as documented.


"""