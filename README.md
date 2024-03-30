# Calculator Application Development Guide

This guide provides step-by-step instructions for creating a simple calculator application that supports basic arithmetic operations, history management, and plugin-based greeting and farewell messages.

## Prerequisites

- Python 3.8 or higher
- Basic knowledge of Python programming
- Familiarity with design patterns is beneficial but not required

## Setup and Structure

1. **Environment Setup**

   Ensure Python 3.8 or higher is installed on your system. You can verify this by running `python --version` in your terminal.
2. **Project Structure**

Create the following directory structure for your project:
 CalculatorApp/
   ├── app/
   │   ├── **init**.py
   │   ├── calculator.py
   │   ├── command_factory.py
   │   ├── commands.py
   │   ├── history_manager.py
   │   └── logger_singleton.py
   ├── plugins/
   ├──     **init**.py
   │   ├── goodbye_plugin.py
   │   └── hello_plugin.py
   |── Tests/
   │   ├── __init__.py
   │   └── test_calculator.py
   ├── info/
   │   ├── logs.csv
   │   └── history.csv
   └── main.py

- The `app` directory contains the core logic of the application.
- The `plugins` directory holds plugins for additional functionality.
- The `info` directory is used for logs and history records.

3. **Initialize a Virtual Environment** (optional but recommended)

   Navigate to your project directory (`CalculatorApp`) and create a virtual environment:

   ```bash
   python -m venv myworld
   ```

   Activate the virtual environment:

   - On Unix or MacOS: `source myworld/bin/activate`

4. **Install Dependencies**

   Currently, this app does not require external dependencies beyond Python's standard library. If you decide to use external libraries, you can install them using pip:

   ```bash
   pip install pandas 
   This wasnt working for me so i did a basic csv structure in my history_manager.py 
   ```

## Implementation

### Core Application (`app/__init__.py`)

1. **Logger Singleton**

   Implement `LoggerSingleton` in `logger_singleton.py` to configure and manage application-wide logging.

2. **Command Pattern**

   Define the `Command` interface and specific command classes (`AddCommand`, `SubtractCommand`, etc.) in `commands.py`.

3. **Factory Method**

   Implement `CommandFactory` in `command_factory.py` to instantiate command objects based on user input.

4. **History Management**

   Create `HistoryManager` in `history_manager.py` for handling calculation history without external dependencies like Pandas.

5. **Application Logic**

   Implement the main application logic in `__init__.py`, integrating the logger, command pattern, and history management.

### Plugins

Implement `hello_plugin.py` and `goodbye_plugin.py` in the `plugins` directory, defining `execute` functions for greeting and farewell messages.

### Main Entry Point (`main.py`)

Set up `main.py` as the entry point of your application, creating an instance of the `App` class and calling its `start` method.

## Running the Application

With all components implemented, run your application:

```bash
python main.py
```

Follow the on-screen prompts to perform calculations, manage history, or exit the application.
