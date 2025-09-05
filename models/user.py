# models/user.py

class User:
    _id_counter = 1

    def __init__(self, name, email):
        self.id = User._id_counter
        User._id_counter += 1
        self.name = name
        self.email = email
        self.projects = []  # list of project IDs / objects

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
