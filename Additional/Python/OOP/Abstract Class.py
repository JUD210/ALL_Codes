# https://www.python-course.eu/python3_abstract_classes.php


""" Why should we use abstract method? 

Think about Animal

| Abstract Class | Abstract Class | Object Class |
| -------------- | -------------- | ------------ |
| Animal ------- | Feline ------- | Lion         |
|        │       |        └------ | Cat          |
|        │       |        └------ | Tiger        |
|        │       |                |              |
|        └------ | Canine ------- | Wolf         |
|                |        └------ | Dog          |

Can you instantiate Animal?

NO!

You can't describe the animal's state.
What is the animal's color? size?, etc...

If you instantiate that 'animal', it's not an animal, but monster.

Object should have 'state' and 'behavior'.


That's why you can't instantiate abstract class.

"""


from abc import ABC, abstractmethod


class AbstractClassExample1(ABC):
    # If there is no @abstractmethod decorator,
    # It's not considered as a abstract class.

    @abstractmethod
    def do_something1(self):
        # You can just use pass.
        pass

    @abstractmethod
    def do_something2(self):
        # or You can implement some codes in abstractmethod.
        print("Some implementation!")


class AnotherSubclass1(AbstractClassExample1):
    def do_something1(self):
        super().do_something1()
        print("The enrichment from AnotherSubclass")

    def do_something2(self):
        super().do_something2()
        print("The enrichment from AnotherSubclass")


class AbstractClassExample2(ABC):
    @abstractmethod
    def override_this(self):
        pass

    @abstractmethod
    def _and_this_too(self):
        pass


class AnotherSubclass2(AbstractClassExample2):
    def override_this(self):
        super().override_this()
        print("The enrichment from AnotherSubclass")


x1 = AnotherSubclass1()
x1.do_something1()
# The enrichment from AnotherSubclass
x1.do_something2()
# Some implementation!
# The enrichment from AnotherSubclass


# x2 = AnotherSubclass2()
# TypeError: Can't instantiate abstract class AnotherSubclass2 with abstract methods _and_this_too

