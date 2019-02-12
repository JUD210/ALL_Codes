# Python don't have public, private, protected. (All public)
# __var_name : imitate private


class Flight:
    def __init__(self, number):
        self.number = number

        # means internal var
        self._number = number

        # means private var
        self.__number = number

    def getnumber(self):
        return self.number

    def get_number(self):
        return self._number

    def get__number(self):
        return self.__number


f = Flight(5)
print(f.getnumber())
# 5
print(f.number)
# 5
print(f.get_number())
# 5
print(f._number)
# 5
print(f.get__number())
# 5
# print(f.__number)
# AttributeError: 'Flight' object has no attribute '__number'
