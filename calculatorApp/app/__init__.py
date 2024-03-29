# Assuming your directory structure remains as previously discussed.
from .logger_singleton import LoggerSingleton
from .command_factory import CommandFactory
from .history_manager import HistoryManager, HistoryManager
from plugins.goodbye_plugin import execute as goodbye_execute
from plugins.hello_plugin import execute as hello_execute 
import os

# Initialize logging through the Singleton pattern
LoggerSingleton.getInstance()

class App:
    def __init__(self):
        # Correctly initialize HistoryManager with the path to history.csv
        self.history_facade = HistoryManager(os.path.join(os.path.dirname(__file__), '..', 'info', 'history.csv'))
        # The rest of your initialization code...

    def start(self):
        user_name = input("Please enter your name: ")
        # Utilizing the hello plugin
        hello_execute(user_name)
        print("Available operations: add, subtract, multiply, divide, exit, clear history, display history")
        
        while True:
            operation = input("\nPlease enter an operation or 'exit' to quit: ").strip().lower()

            if operation == 'exit':
                goodbye_execute(user_name)  # Execute goodbye plugin directly here
                break
            elif operation == 'clear history':
                self.history_facade.clear_history()
                print("History cleared.")
                continue
            elif operation == 'display history':
                self.history_facade.display_history()
                continue

            # Create and execute command
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                command = CommandFactory.get_command(operation)
                result = command.execute(num1, num2)
                print(f"The result is {result}")
                # Adding record to history
                self.history_facade.add_record(user_name, f"{num1} {operation} {num2}", result)
            except ValueError as e:
                print(f"An error occurred: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
