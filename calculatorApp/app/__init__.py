import logging
import csv
import os
from .calculator import add, subtract, multiply, divide
from plugins.goodbye_plugin import execute as goodbye_execute
from plugins.hello_plugin import execute as hello_execute 

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
        
        logging.info(f"{user_name} started the Calculator App")
        
        hello_execute(user_name)
        print("Available operations: add, subtract, multiply, divide, exit")
        
        while True:
            operation = input("\nPlease enter an operation or 'exit' to quit: ").strip().lower()

            if operation == 'exit':
                logging.info(f"{user_name} exited the application.")
                goodbye_execute(user_name)  # Execute goodbye plugin directly here
                break

            if operation not in ['add', 'subtract', 'multiply', 'divide']:
                print("Invalid operation. Please choose a valid operation.")
                continue

            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                extra = {'username': user_name}
                logging.info(f"Operation {operation} with numbers {num1} and {num2}", extra=extra)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            try:
                result = {'add': add, 'subtract': subtract, 'multiply': multiply, 'divide': divide}[operation](num1, num2)
                print(f"The result is {result}")
                logging.info(f"Result of {operation}: {result}", extra=extra)
            except ValueError as e:
                print(e)
                continue
            except KeyError:
                print("An unexpected error occurred.")
