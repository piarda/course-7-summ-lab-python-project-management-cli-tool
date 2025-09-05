# models/task.py

from models.entity import Entity

class Task(Entity):
    def __init__(self, title, status, assigned_to, project_title):
        super().__init__()
        self.title = title
        self.status = status
        self.assigned_to = assigned_to
        self.project_title = project_title

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
