class A(object):
    def foo(self, x):
        print(f"executing foo({self},{x})")

    @classmethod
    def class_foo(cls, x):
        print(f"executing foo({cls},{x})")

    @staticmethod
    def static_foo(x):
        print(f"executing foo({x})")


a = A()

a.foo(5)
# executing foo(<__main__.A object at 0x000001B0E9544278>,5)
a.class_foo(6)
# executing foo(<class '__main__.A'>,6)
a.static_foo(7)
# executing foo(7)

# A.foo(5)
# TypeError: foo() missing 1 required positional argument: 'x'
A.class_foo(6)
# executing foo(<class '__main__.A'>,6)
A.static_foo(7)
# executing foo(7)


#############################################


class Language:
    default_language = "English"

    def __init__(self):
        self.show = "My language is: " + self.default_language

    @classmethod
    def class_my_language(cls):
        return cls()

    @staticmethod
    def static_my_language():
        return Language()

    def print_language(self):
        print(self.show)


class KoreanLanguage(Language):
    default_language = "Korean"


l1 = KoreanLanguage.static_my_language()
l1.print_language()
# My language is: English

l2 = KoreanLanguage.class_my_language()
l2.print_language()
# My language is: Korean
