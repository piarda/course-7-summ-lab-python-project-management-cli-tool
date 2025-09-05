# models/project.py

class Project:
    _id_counter = 1

    def __init__(self, title, description, due_date, user_name):
        self.id = Project._id_counter
        Project._id_counter =+ 1
        self.title = title
        self.description = description
        self.due_date = due_date
        self.user_name = user_name
        self.tasks = []

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
