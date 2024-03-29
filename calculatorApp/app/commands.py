class Command:
    def execute(self, *args):
        raise NotImplementedError

class AddCommand(Command):
    def execute(self, num1, num2):
        return num1 + num2

class SubtractCommand(Command):
    def execute(self, num1, num2):
        return num1 - num2

class MultiplyCommand(Command):
    def execute(self, num1, num2):
        return num1 * num2

class DivideCommand(Command):
    def execute(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
