
""" Duck Typing 

If it walks like a duck and it quacks like a duck, then it must be a duck.

"""

class Parrot:
    def fly(self):
        print("Parrot flying")


class Airplane:
    def fly(self):
        print("Airplane flying")


class Whale:
    def swim(self):
        print("Whale swimming")


def lift_off(entity):
    entity.fly()


parrot = Parrot()
airplane = Airplane()
whale = Whale()


lift_off(parrot)
# prints `Parrot flying`

lift_off(airplane)
# prints `Airplane flying`

# lift_off(whale)
# AttributeError: 'Whale' object has no attribute 'fly'
