# tests/test_history_manager.py
import os
from app.history_manager import HistoryManager

def test_history_manager(tmp_path):
    # Use tmp_path to avoid cluttering your project with test files
    history_file = tmp_path / "test_history.csv"
    manager = HistoryManager(str(history_file))

    # Test adding a record
    manager.add_record("user1", "add 1 2", 3)
    assert len(manager.history) == 1
    assert manager.history[0]["Operation"] == "add 1 2"
    assert manager.history[0]["Result"] == "3"

    # Test clearing history
    manager.clear_history()
    assert len(manager.history) == 0

    # Ensure the file is updated (implicitly tests _save_history)
    assert history_file.read_text() == "User Name,Operation,Result\n"
