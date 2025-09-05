# models/task.py

from models.entity import Entity

class Task(Entity):
    VALID_STATUSES = {"incomplete", "complete"}

    def __init__(self, title, status, assigned_to, project_title):
        super().__init__()
        self.title = title
        self.status = status
        self.assigned_to = assigned_to
        self.project_title = project_title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value or not value.strip():
            raise ValueError("Task title cannot be empty.")
        self._title = value.strip()
        
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in self.VALID_STATUSES:
            raise ValueError(f"Invalid status '{value}'. Valid options are: {self.VALID_STATUSES}")
        self._status = value

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to,
            "project_title": self.project_title
        }
    
    @classmethod
    def from_dict(cls, data):
        task = cls(
            data["title"],
            data["status"],
            data["assigned_to"],
            data["project_title"]
        )
        task.id = data["id"]
        return task

    def __str__(self):
        return f"[{self.id}] {self.title} | {self.status} | Assigned to: {self.assigned_to} | Project: {self.project_title}"
