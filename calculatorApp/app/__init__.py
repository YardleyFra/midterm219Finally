from .logger_singleton import LoggerSingleton
from .command_factory import CommandFactory
from .history_manager import HistoryManager
from plugins.goodbye_plugin import execute as goodbye_execute
from plugins.hello_plugin import execute as hello_execute 
import os

# Initialize logging through the Singleton pattern
LoggerSingleton.getInstance()

class App:
    def __init__(self):
        # Correctly initialize HistoryManager with the path to history.csv
        self.history_facade = HistoryManager(os.path.join(os.path.dirname(__file__), '..', 'info', 'history.csv'))

    def start(self):
        user_name = input("Please enter your name: ")
        hello_execute(user_name)
        print("Welcome to the Calculator App, " + user_name)
        print("Available operations: add, subtract, multiply, divide, exit, clear history, display history")
        
        while True:
            operation = input("\nPlease enter an operation or 'exit' to quit: ").strip().lower()

            if operation == 'exit':
                goodbye_execute(user_name)
                break
            elif operation == 'clear history':
                self.history_facade.clear_history()
                print("History cleared.")
                continue
            elif operation == 'display history':
                self.history_facade.display_history()
                continue

            try:
                num1 = self._prompt_for_number("Enter the first number: ")
                num2 = self._prompt_for_number("Enter the second number: ")
                command = CommandFactory.get_command(operation)
                if command:
                    result = command.execute(num1, num2)
                    print(f"The result is {result}")
                    self.history_facade.add_record(user_name, f"{num1} {operation} {num2}", result)
                else:
                    print("Invalid operation. Please choose a valid operation.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    def _prompt_for_number(self, message):
        """Prompt the user repeatedly until a valid number is entered."""
        while True:
            try:
                return float(input(message))
            except ValueError:
                print("Please enter a valid numerical value.")
