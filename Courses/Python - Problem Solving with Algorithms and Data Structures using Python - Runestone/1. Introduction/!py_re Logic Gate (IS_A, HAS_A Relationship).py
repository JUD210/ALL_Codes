# https://runestone.academy/runestone/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html


# !TODO: Study Again!


from abc import abstractmethod

# UnaryGate IS-A LogicGate (IS-A Relationship)
# Require Inheritance

# Connector HAS-A LogicGate (HAS-A Relationship)
# No Require Inheritance


# Inputs
standard_input = """0
0
0
0
1
1
0
1"""


class LogicGate:
    def __init__(self, label):
        self.label = label.upper()
        self.__output = None

    @property
    def output(self):
        self.__output = self.perform_gate_logic()
        return self.__output

    @abstractmethod
    def perform_gate_logic(self):
        pass


############################################################


class BinaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)

        self.__pin_a = None
        self.__pin_b = None

    @property
    def pin_a(self):
        if self.__pin_a is None:
            return int(input(f"Enter Pin A input for gate {self.label} --> "))
        else:
            return self.__pin_a.from_gate.output

    @property
    def pin_b(self):
        if self.__pin_b is None:
            return int(input(f"Enter Pin B input for gate {self.label} --> "))
        else:
            return self.__pin_b.from_gate.output

    def set_next_pin(self, connector):
        if self.__pin_a is None:
            self.__pin_a = connector
        elif self.__pin_b is None:
            self.__pin_b = connector
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class UnaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)

        self.__pin = None

    @property
    def pin(self):
        if self.__pin is None:
            return int(input(f"Enter Pin input for gate {self.label} --> "))
        else:
            return self.__pin.from_gate.output

    def set_next_pin(self, connector):
        if self.__pin is None:
            self.__pin = connector
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


############################################################


class AndGate(BinaryGate):
    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        a = self.pin_a
        b = self.pin_b

        # Warning! Never replace
        # a == 1 and b == 1
        # to
        # self.pin_a ==1 and self.pin_b ==1
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        a = self.pin_a
        b = self.pin_b

        # Warning! Never replace
        # a == 1 or b == 1
        # to
        # self.pin_a ==1 or self.pin_b ==1
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NotGate(UnaryGate):
    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        if self.pin:
            return 0
        else:
            return 1


############################################################


class Connector:
    def __init__(self, fgate, tgate):
        self.__from_gate = fgate
        self.__to_gate = tgate

        tgate.set_next_pin(self)

    @property
    def from_gate(self):
        return self.__from_gate

    @property
    def to_gate(self):
        return self.__to_gate


g1 = AndGate("g1")
g2 = AndGate("g2")
g3 = OrGate("g3")
g4 = NotGate("g4")

c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)

print(g4.output)
