import logging
import csv
import os
import importlib.util
from .calculator import add, subtract, multiply, divide

def load_and_execute_plugins(plugin_dir, user_name):
    for filename in os.listdir(plugin_dir):
        if filename.endswith('.py') and not filename == '__init__.py':
            plugin_path = os.path.join(plugin_dir, filename)
            module_name = os.path.splitext(filename)[0]

            spec = importlib.util.spec_from_file_location(module_name, plugin_path)
            plugin_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(plugin_module)

            # Assuming each plugin module has an 'execute' function
            if hasattr(plugin_module, 'execute'):
                plugin_module.execute(user_name)

class CSVLogHandler(logging.StreamHandler):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def emit(self, record):
        
        username = getattr(record, 'username', 'Unknown') 
        message = self.format(record)
        with open(self.filename, 'a', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([username, message])



log_path = os.path.join(os.path.dirname(__file__), '..', 'info', 'logs.csv')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s, %(levelname)s, %(message)s',
                    handlers=[CSVLogHandler(log_path)])

class App:
    def start(self):
        user_name = input("Please enter your name: ")
        plugins_dir = os.path.join(os.path.dirname(__file__), '..', 'plugins')
        load_and_execute_plugins(plugins_dir, user_name)
        logging.info(f"{user_name} started the Calculator App")
        
        print("Available operations: add, subtract, multiply, divide, exit")
        
        while True:
            operation = input("\nPlease enter an operation or 'exit' to quit: ").strip().lower()

            if operation == 'exit':
                logging.info(f"{user_name} exited the application.")
                print("Thank you for using the Calculator App. Goodbye!")
                break

            if operation not in ['add', 'subtract', 'multiply', 'divide']:
                print("Invalid operation. Please choose a valid operation.")
                continue

            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                # Include the username in each log by modifying the log record directly
                extra = {'username': user_name}
                logging.info(f"Operation {operation} with numbers {num1} and {num2}", extra=extra)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            # Perform the operation
            try:
                if operation == 'add':
                    result = add(num1, num2)
                elif operation == 'subtract':
                    result = subtract(num1, num2)
                elif operation == 'multiply':
                    result = multiply(num1, num2)
                elif operation == 'divide':
                    try:
                        result = divide(num1, num2)
                    except ValueError as e:
                        print(e)
                        continue

                print(f"The result is {result}")
                logging.info(f"Result of {operation}: {result}", extra=extra)
            except Exception as e:
                logging.exception(f"An error occurred during {operation}.", extra=extra)
