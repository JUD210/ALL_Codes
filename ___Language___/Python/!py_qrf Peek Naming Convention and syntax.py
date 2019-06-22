# https://~~~ (References)


from abc import abstractmethod

""" This is for abstract class and method """


from typing import Any, List, Tuple, Set, Dict, NamedTuple  # noqa

# noqa disables flake8 linter in a single line.

""" This is for mypy linter's advanced static type checking

The static type definition is able from Python 3.6


    Should I use static type checking in my own code?

Well, it's not an all-or-nothing question. Luckily, Python supports the concept of gradual typing. This means that I can gradually introduce types into my code.

Code without type hints will be ignored by the static type checker. Therefore, I can start adding types to critical components, and continue as long as it adds value to me.


    Type annotation example

def func(arg: arg_type_annotation, optarg: arg_type_annotation = default) -> return_type_annotation:
    #...
    pass

"""

# Variable Annotation while undefined
standard_input: str

# print(standard_input)
# NameError: name 'standard_input' is not defined


standard_input = """4
This is for
AREPL for Python
Extension's
Automatic Input"""


CONSTANT_NAME: int = 123_456_789
# for mypy linter's static type checking


# fmt:off
# This comment disable code formatting
#
# fmt:on
# This comment enable code formatting
#
### As I use the wonderful formatter 'Black', sometimes it does unnecessary formatting.


""" I prefer Top-Down order for classes because it allows quick peek.

Top

############################################################

Middle 1
Middle 2

############################################################

Bottom 11
Bottom 12
Bottom 21
Bottom 22

"""


############################################################


class TopHierarchy:
    """ I prefer this order for inner part of a class.

    Class Var

    ############################################################

    __init__ (with Instance Var), Magic Methods

    ############################################################

    # Property  # If I "have to" use getter/setter

    ############################################################

    public, private, abstract, class, static method

    """

    class_var = "some_value"

    ############################################################

    def __init__(self, *args: str):
        self.public_var = args[0]
        self._internal_var = args[1]
        self.__private_var = args[2]

        """ The Meaning of '_' and '__'.

        # https://dbader.org/blog/meaning-of-underscores-in-python

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
        : Triggers name mangling(dunder) when used in a class context. Enforced by the Python interpreter.

        __var__
        : Indicates special methods defined by the Python language. Avoid this naming scheme for your own attributes.

        _
        : Sometimes used as a name for temporary or insignificant variables ("don't care").
        : Also, The result of the last expression in a Python REPL.

        """

    def __str__(self) -> str:
        # for mypy linter's static type checking

        # return instance's vars when print(instance_name)
        return f"vars : {self.__dict__}"

    @property
    def private_var(self):  # Treat it as a @private_var.getter
        return self.__private_var

    @private_var.setter
    def private_var(self, value):
        self.__private_var = value

    @private_var.deleter
    def private_var(self):
        del self.__private_var

    """ I'm not gonna use getter/setter because it's not pythonic way.

    I'd definitely stick with the Zen of Python's "Simple is better than complex."


        But, If I need to use getter/setter, I'll use property instead.

    It's more advanced, simple, and pythonic getter/setter because it
    makes able to use getter/settered variable like a public variable.


        See below example.

    instance_name.private_var = 255
    print(instance_name.private_var)
    # 255


    ############################################################

        Is it pythonic to use properties to limit the mutability of class attributes (variables and methods)?

    For attributes/properties/variables at either the class or instance level: yes, absolutely! The decorator @property is built in specifically to give control over read, write, and delete. Common use cases include:

    - enforcing read-only or write-only
    - ensuring valid values
    - ensuring consistency with other state
    - presenting limited internal state in multiple ways
    - triggering other system logic
    - persistence


        But really the most authoritative I can get is to quote PEP-8, the Python style guide.

    For simple public data attributes, it is best to expose just the attribute name, without complicated accessor/mutator methods. Keep in mind that Python provides an easy path to future enhancement, should you find that a simple data attribute needs to grow functional behavior.

    In that case, use properties to hide functional implementation behind simple data attribute access syntax.

    """
    ######################################################################

    def public_method(self, *args, **kwargs):
        # ...
        pass

    def __private_method(self, *args, **kwargs):
        # almost same concept like __private_var
        pass

    ######################################################################

    # If I define abstractmethod, this class become abstract class.
    @abstractmethod
    def abstract_method(self, *args, **kwargs):
        """ Concept of Abstract Class.

        # https://www.python-course.eu/python3_abstract_classes.php
        (for detail description)

        Think about Animal

        | Abstract Class | Abstract Class | Object Class |
        | -------------- | -------------- | ------------ |
        | Animal ------- | Feline ------- | Lion         |
        |        |       |        |------ | Cat          |
        |        |       |        |------ | Tiger        |
        |        |       |                |              |
        |        |------ | Canine ------- | Wolf         |
        |                |        |------ | Dog          |

        Can you instantiate Animal?

        NO!

        You can't describe the Animal's state and behavior.
        What is the Animal's color? size?,...
        What does the Animal do? eat? run? talk?,...

        If you instantiate that 'Animal' class, it's not an animal, but monster!

        Object should have 'state' and 'behavior'.


        That's the reason why you can't instantiate abstract class.

        """
        # ...
        pass

    @classmethod
    def class_method(cls, *args, **kwargs):
        """ About class method.

        A class method is a method that is bound to a class rather than its object. It doesn't require creation of a class instance, much like staticmethod.

        The difference between a static method and a class method is:


        Static method knows nothing about the class and just deals with the parameters

        Class method works with the class since its parameter is always the class itself.

        The class method can be called both by the class and its object.

        Class.classmethod()
        Or even
        Class().classmethod()

        But no matter what, the class method is always attached to a class with first argument as the class itself cls.

        def classMethod(cls, args...)
            pass

        """
        # ...
        pass

    @staticmethod
    def static_method(*args, **kwargs):
        """ About static method.

        Static methods, much like class methods, are methods that are bound to a class rather than its object.

        They do not require a class instance creation. So, are not dependent on the state of the object.

        The difference between a static method and a class method is:


        Static method knows nothing about the class and just deals with the parameters.

        Class method works with the class since its parameter is always the class itself.

        They can be called both by the class and its object.

        Class.staticmethodFunc()
        or even
        Class().staticmethodFunc()
        """
        # ...
        pass


############################################################


class MiddleHierarchy1(TopHierarchy):
    # ...
    pass


class MiddleHierarchy2(TopHierarchy):
    # ...
    pass


############################################################


class BottomHierarchy11(MiddleHierarchy1):
    def __init__(self, *args: str, **kwargs: Any):
        super().__init__(*args)

        if kwargs.get("override_var"):
            self.public_var = "Overridden 1"
            self._internal_var = "Overridden 2"
            # self.__private_var = "Overridden 3"
            # AttributeError occurs: this object has no attribute '__private_var'
            self._TopHierarchy__private_var = "Overridden 3"

    def abstract_method(self, *args, **kwargs):
        # ...
        pass


class BottomHierarchy12(MiddleHierarchy1):
    # ...
    pass


class BottomHierarchy21(MiddleHierarchy2):
    # ...
    pass


class BottomHierarchy22(MiddleHierarchy2):
    # ...
    pass


############################################################


def function_name(arg_name1, arg_name2, keyword="value"):
    # ...
    pass


############################################################


# if __name__ == "__main__":
#
# '__main__' is the name of the scope in which top-level code executes. A module's __name__ is set equal to '__main__' when read from standard input, a script, or from an interactive prompt.


# fmt: off
_, _, global_var_name1, global_var_name2, global_var_name3 = ("-1", 0, "1", "2", "3")  # type: ignore

# I'll use type: ignore comment when I use temporary variable '_'
# Because it could cause below  error.
#
# [mypy] Incompatible types in assignment (expression has type "int", variable has type "str") [error]

# fmt: on


is_override_var_mode = False

print(
    f"{global_var_name1}, {global_var_name2}, {global_var_name3}, {is_override_var_mode}",
    sep="\n",
)
# 1, 2, 3, False


instance_name = BottomHierarchy11(
    global_var_name1, global_var_name2, global_var_name3, override=is_override_var_mode
)
# ==
# instance_name = BottomHierarchy11("1", "2", "3", False)


print(f"{instance_name}")
# vars : {'public_var': '1', '_internal_var': '2', '_TopHierarchy__private_var': '3'}
print(f"{BottomHierarchy11('1','2','3',override_var=True)}")
# vars : {'public_var': 'Overridden 1', '_internal_var': 'Overridden 2', '_TopHierarchy__private_var': 'Overridden 3'}


print(
    f"""
{'public_var' in dir(instance_name)}
{'_internal_var' in dir(instance_name)}
{'__private_var' in dir(instance_name)}
{'_TopHierarchy__private_var' in dir(instance_name)}
"""
)
#
# True
# True
# False
# True
#

for _ in range(int(input())):  # type: ignore
    # 4
    line = input().split()
    # This is for
    # AREPL for Python
    # Extension's
    # Automatic Input

    print("\n".join([word for word in line]))
    # This
    # is
    # for

    # AREPL
    # for
    # Python

    # Extension's

    # Automatic
    # Input


################################################################################
# REFERNCE
#
# https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html
# https://www.datacamp.com/community/tutorials/pep8-tutorial-python-code
# https://www.python.org/dev/peps/pep-0008/#naming-conventions
# https://medium.com/@dasagrivamanu/python-naming-conventions-the-10-points-you-should-know-149a9aa9f8c7

"""

1. General
Avoid names that are too general or too wordy. Strike a good balance between the two.
Bad: data_structure, my_list, info_map, dictionary_for_the_purpose_of_storing_data_representing_word_definitions
Good: user_profile, menu_options, word_definitions
Don't be a jackass and name things "O", "l", or "I"
When CamelCase names, capitalize all letters of an abbreviation (e.g. HTTPServer)

2. Packages
Package names should be all lower case
When multiple words are needed, an underscore should separate them
It is usually preferable to stick to 1 word names

3. Modules
Module names should be all lower case
When multiple words are needed, an underscore should separate them
It is usually preferable to stick to 1 word names

4. Classes
Class names should follow the UpperCaseCamelCase convention
Python's built-in classes, however are typically lowercase words
Exception classes should end in "Error"

5. Global (module-level) vars
Global vars should be all lowercase
Words in a global var name should be separated by an underscore

6. Instance vars
Instance var names should be all lower case
Words in an instance var name should be separated by an underscore
Non-public instance vars should begin with a single underscore
If an instance name needs to be mangled, two underscores may begin its name

7. Methods
Method names should be all lower case
Words in an method name should be separated by an underscore
Non-public method should begin with a single underscore
If a method name needs to be mangled, two underscores may begin its name

8. Method Arguments
Instance methods should have their first argument named 'self'.
Class methods should have their first argument named 'cls'

9. Functions
Function names should be all lower case
Words in a function name should be separated by an underscore

10. Constants
Constant names must be fully capitalized
Words in a constant name should be separated by an underscore

"""


# https://stackoverflow.com/questions/10289461/what-is-a-good-way-to-order-methods-in-a-python-class

"""
As others have pointed out, there is no right way to order your methods. Maybe a PEP suggestion would be useful, but anyway. Let me try to approach your question as objectively as possible.

Interfaces first: Public methods and Python magic functions define the interface of the class. Most of the time, you and other developers want to use a class rather than change it. Thus they will be interested in the interface of that class. Putting it first in the source code avoids scrolling through implementation details you don't care about.

Properties, magic methods, public methods: It's hard to define the best order between those three, which are all part of the interface of the class. As @EthanFurman says, it's most important to stick with one system for the whole project. Generally, people expect __init__() to the best first function in the class so I follow up with the other magic methods right below.

Reading order: Basically, there are two ways to tell a story: Bottom-up or top-down. By putting high-level functions first, a developer can get a rough understanding of the class by reading the first couple of lines. Otherwise, one would have to read the whole class in order to get any understanding of the class and most developers don't have the time for that. As a rule of thumb, put methods above all methods called from their body.

Class methods and static methods: Usually, this is implied by the reading order explained above. Normal methods can call all methods times and thus come first. Class methods can only call class methods and static methods and come next. Static methods cannot call other methods of the class and come last.

Hope this helps. Most of these rules are not Python-specific by the way. I'm not aware of a language that enforces method order but if so, it would be quite interesting and please comment.
"""
