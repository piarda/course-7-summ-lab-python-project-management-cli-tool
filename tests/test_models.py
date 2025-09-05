# tests/test_models.py

import pytest
from models.user import User
from models.project import Project
from models.task import Task

def test_user_creation():
    user = User("Matt", "matt@example.com")
    assert user.name == "Matt"
    assert user.email == "matt@example.com"
    assert user.id is not None
    assert str(user).startswith(f"[{user.id}] Matt")

def test_project_creation_and_due_date_validation():
    project = Project("Build App", "Description", "2025-12-31", "Matt")
    assert project.title == "Build App"
    assert project.due_date == "2025-12-31"
    
    with pytest.raises(ValueError):
        project.due_date = "invalid-date"

def test_task_creation():
    task = Task("Write tests", "incomplete", "Matt", "Build App")
    assert task.title == "Write tests"
    assert task.status == "incomplete"
    assert task.assigned_to == "Matt"
    assert task.project_title == "Build App"
