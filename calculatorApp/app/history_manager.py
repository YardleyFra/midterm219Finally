import csv
import os

class HistoryManager:
    def __init__(self, path):
        self.path = path
        self.history = []
        self._load_history()

    def _load_history(self):
        if os.path.exists(self.path):
            with open(self.path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                self.history = list(reader)
        else:
            self.history = []

    def add_record(self, user_name, operation, result):
        # Include user_name in the new record
        new_record = {'User Name': user_name, 'Operation': operation, 'Result': str(result)}
        self.history.append(new_record)
        self._save_history()

    def _save_history(self):
        # Ensure 'User Name' is included in the fieldnames for the CSV
        with open(self.path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['User Name', 'Operation', 'Result'])
            writer.writeheader()
            for record in self.history:
                writer.writerow(record)

    def clear_history(self):
        self.history = []
        self._save_history()

    def display_history(self):
        for index, record in enumerate(self.history):
            # Update the display format to include the user's name
            print(f"{index}: {record['User Name']} - {record['Operation']} = {record['Result']}")
