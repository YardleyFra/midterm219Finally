# tests/test_commands.py
import pytest
from app.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add_command():
    command = AddCommand()
    assert command.execute(1, 2) == 3

def test_subtract_command():
    command = SubtractCommand()
    assert command.execute(5, 3) == 2

def test_multiply_command():
    command = MultiplyCommand()
    assert command.execute(2, 4) == 8

def test_divide_command():
    command = DivideCommand()
    assert command.execute(8, 2) == 4
    with pytest.raises(ValueError):
        command.execute(8, 0)  # Division by zero should raise a ValueError
