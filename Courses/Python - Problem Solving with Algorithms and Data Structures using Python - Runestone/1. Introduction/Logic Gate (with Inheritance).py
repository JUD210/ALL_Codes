# https://runestone.academy/runestone/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html


from abc import ABC, abstractmethod


class LogicGate:
    def __init__(self, label):
        self.__label = label
        self.__output = None

    def get_label(self):
        return self.__label

    def get_output(self):
        self.__output = self.perform_gate_logic()
        return self.__output

    @abstractmethod
    def perform_gate_logic(self):
        pass


class BinaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)

        self.__pin_a = None
        self.__pin_b = None

    def get_pin_a(self, num=None):
        if num == None:
            return int(input(f"Enter Pin A input for gate {self.get_label()} --> "))
        else:
            return num

    def get_pin_b(self, num=None):
        if num == None:
            return int(input(f"Enter Pin A input for gate {self.get_label()} --> "))
        else:
            return num


class UnaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)

        self.__pin = None

    def get_pin(self):
        return int(input(f"Enter Pin input for gate {self.get_label()} --> "))


class AndGate(BinaryGate):
    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

    # def show_demo(self):
    #     print(
