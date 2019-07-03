# https://dbader.org/blog/meaning-of-underscores-in-python


""" Summary

|                Pattern                 | Example |
| -------------------------------------- | ------- |
| Single Leading Underscore              | _var    |
| Single Trailing Underscore             | var_    |
| Double Leading Underscore              | __var   |
| Double Leading and Trailing Underscore | __var__ |
| Single Underscore                      | _       |

_var
: Naming convention indicating a name is meant for internal use. Generally not enforced by the Python interpreter (except in wildcard imports) and meant as a hint to the programmer only. |

var_
: Used by convention to avoid naming conflicts with Python keywords.

__var
: Triggers name mangling when used in a class context. Enforced by the Python interpreter.

__var__
: Indicates special methods defined by the Python language. Avoid this naming scheme for your own attributes.

_
: Sometimes used as a name for temporary or insignificant variables ("don't care").
: Also, The result of the last expression in a Python REPL.

"""

######################################################################

"""

### Single Leading Underscore: _var

Single underscores are a Python naming convention indicating a name is meant for internal use. It is generally not enforced by the Python interpreter and meant as a hint to the programmer only.



### Single Trailing Underscore: var_

A single trailing underscore (postfix) is used by convention to avoid naming conflicts with Python keywords.



### Double Leading Underscore: __var

class ManglingTest:
    def __init__(self):
        self.__mangled = 'hello'

    def get_mangled(self):
        return self.__mangled

>>> ManglingTest().get_mangled()
'hello'
>>> ManglingTest().__mangled
AttributeError: "'ManglingTest' object has no attribute '__mangled'"


class MangledMethod:
    def __method(self):
        return 42

    def call_it(self):
        return self.__method()

>>> MangledMethod().__method()
AttributeError: "'MangledMethod' object has no attribute '__method'"
>>> MangledMethod().call_it()
42



### Double Leading and Trailing Underscore: __var__

Names that have both leading and trailing double underscores are reserved for special use in the language. This rule covers things like __init__ for object constructors, or __call__ to make an object callable.

These dunder methods are often referred to as magic methods-but many people in the Python community, including myself, don't like that.

It's best to stay away from using names that start and end with double underscores ("dunders") in your own programs to avoid collisions with future changes to the Python language.



### Single Underscore: _

Per convention, a single standalone underscore is sometimes used as a name to indicate that a variable is temporary or insignificant even though it's simply a valid variable name.

>>> car = ('red', 'auto', 12, 3812.4)
>>> color, _, _, mileage = car

>>> color
'red'
>>> mileage
3812.4
>>> _
12


Besides its use as a temporary variable, "_" is a special variable in most Python REPLs that represents the result of the last expression evaluated by the interpreter.

This is handy if you're working in an interpreter session and you'd like to access the result of a previous calculation. Or if you're constructing objects on the fly and want to interact with them without assigning them a name first:

>>> 20 + 3
23
>>> _
23
>>> print(_)
23

>>> list()
[]
>>> _.append(1)
>>> _.append(2)
>>> _.append(3)
>>> _
[1, 2, 3]


"""
