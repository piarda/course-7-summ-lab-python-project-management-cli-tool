# models/project.py

from datetime import datetime
from models.entity import Entity

class Project(Entity):
    def __init__(self, title, description, due_date, user_name):
        super().__init__()
        self.title = title  # Validates via Setter
        self.description = description
        self.due_date = due_date    # Validates via Setter
        self.user_name = user_name
        self.tasks = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value.strip() if value else ""

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Due date must be in YYYY-MM-DD format.")
        self._due_date = value

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "user_name": self.user_name,
            "tasks": self.tasks
        }
    
    @classmethod
    def from_dict(cls, data):
        project = cls(
            data["title"],
            data["description"],
            data["due_date"],
            data["user_name"]
        )
        project.id = data["id"]
        project.tasks = data.get("tasks", [])
        return project

    def __str__(self):
        return f"[{self.id}] {self.title} (Due: {self.due_date}) - User: {self.user_name}"
