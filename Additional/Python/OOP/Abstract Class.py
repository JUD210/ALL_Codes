# https://www.python-course.eu/python3_abstract_classes.php


""" Concept of Abstract Class.

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


from abc import ABC, abstractmethod


class AbstractClassExample1(ABC):
    # If there is no @abstractmethod decorator, It's not considered as a abstract class.

    # If you use Abstract Method, you MUST override that method, or you will get some error.
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

# Yeah. If you use Abstract Method, you MUST override that method, or you will get some error.
