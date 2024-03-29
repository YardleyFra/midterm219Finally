from .commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class CommandFactory:
    @staticmethod
    def get_command(operation):
        if operation == "add":
            return AddCommand()
        elif operation == "subtract":
            return SubtractCommand()
        elif operation == "multiply":
            return MultiplyCommand()
        elif operation == "divide":
            return DivideCommand()
        else:
            raise ValueError("Unknown operation")
