# tests/test_command_factory.py
from app.command_factory import CommandFactory
from app.commands import AddCommand, SubtractCommand

def test_command_factory():
    add_command = CommandFactory.get_command("add")
    assert isinstance(add_command, AddCommand)
    
    subtract_command = CommandFactory.get_command("subtract")
    assert isinstance(subtract_command, SubtractCommand)
    
    # Test for an invalid command
    with pytest.raises(ValueError):
        CommandFactory.get_command("invalid")
