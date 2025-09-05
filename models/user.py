# models/user.py

from models.entity import Entity

class User(Entity):
    def __init__(self, name, email):
        super().__init__()
        self.name = name
        self._email = None  # Protected attribute
        self.email = email  # Use setter to validate
        self.projects = []

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email address")
        self._email = value

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
    
    @classmethod
    def from_dict(cls, data):
        user = cls(data["name"], data["email"])
        user.id = data["id"]
        return user

    def __str__(self):
        return f"[{self.id}] {self.name} ({self.email})"
