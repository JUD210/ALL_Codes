"""
About whether or not we can change an object once it has been created.

[Mutable objects]
list, dict, set, byte array

[Immutable objects (Hashable)]
int, float, complex, boolean, string, tuple, frozen set (immutable version of set), bytes

In Python, any immutable object is hashable, meaning its value does not change during its lifetime. This allows Python to create a unique hash value to identify it, which can be used by dictionaries to track unique keys and sets to track unique values. This is why Python requires us to use immutable datatypes for the keys in a dictionary.
"""

""" identity """
print("\n=== Identity ===")
a = "Holberton"
b = "Holberton"
c = a

print(id(a))  # 140135
print(id(b))  # 140135
print(id(c))  # 140135

print(a is b)  # True
print(a is c)  # True

a = "Mini"
b = "Hyugi"

print(id(a))  # 180135
print(id(b))  # 153435

print(a is b)  # False


""" Immutable Object's Characteristics """
print("\n=== Immutable ===")

x = 10
y = x

print(id(x) == id(y))  # True
print(id(y) == id(10))  # True

x += 1

print(id(x) == id(y))  # False
print(id(y) == id(10))  # True


""" Mutable Object's Characteristics """
print("\n=== Mutable ===")

fruits = ['apple', 'banana', 'kiwi']
mutability_test = fruits
mutability_test[2] = 'watermelon'

print(fruits)
print(mutability_test)
# ['apple', 'banana', 'watermelon']
# ['apple', 'banana', 'watermelon']

# Either variable can be used to 'access' that list object.


"""Exceptions in immutability

Not all of the immutable objects are actually immutable. Confused? Let me explain.

As discussed earlier, Python containers liked tuples are immutable. That means value of a tuple can't be changed after it is created. But the "value" of a tuple is infact a sequence of names with unchangeable bindings to objects. The key thing to note is that the bindings are unchangeable, not the objects they are bound to.

Let us consider a tuple t = (‘holberton’, [1, 2, 3])

The above tuple t contains elements of different data types, the first one is an immutable string and the second one is a mutable list.The tuple itself isn’t mutable. i.e. it doesn’t have any methods for changing its contents. Likewise, the string is immutable because strings don’t have any mutating methods. But the list object does have mutating methods, so it can be changed. This is a subtle point, but nonetheless important: the “value” of an immutable object can’t change, but it’s constituent objects can."""


"""How objects are passed to Functions

Its important for us to know difference between mutable and immutable types and how they are treated when passed onto functions .Memory efficiency is highly affected when the proper objects are used.

For example if a mutable object is called by reference in a function, it can change the original variable itself. Hence to avoid this, the original variable needs to be copied to another variable. Immutable objects can be called by reference because its value cannot be changed anyways.
"""


def updateList(list1):
    list1 += [10]


n = [5, 6]
print(id(n))  # 1403121
updateList(n)
print(n)      # [5, 6, 10]
print(id(n))  # 1403121

"""
As we can see from the above example, we have called the list via call by reference, so the changes are made to the original list itself.
"""


def updateNumber(n):
    print(id(n))
    n += 10


b = 5
print(id(b))     # 10055680
updateNumber(b)  # 10055680
print(b)         # 5

"""
In the above example the same object is passed to the function, but the variables value doesn’t change even though the object is identical. This is called pass by value. So what is exactly happening here? When the value is called by the function, only the value of the variable is passed, not the object itself. So the variable referencing the object is not changed, but the object itself is being changed but within the function scope only. Hence the change is not reflected.
"""
