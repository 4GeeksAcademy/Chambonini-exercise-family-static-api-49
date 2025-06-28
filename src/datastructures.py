import random

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "Tommy",
                "last_name": self.last_name,
                "age": 25,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Sarah",
                "last_name": self.last_name,
                "age": 30,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    def _generate_id(self):
        return random.randint(0, 99999999)

    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generate_id()
        member["last_name"] = self.last_name
        self._members.append(member)

    def delete_member(self, id):
        self._members = [m for m in self._members if m["id"] != id]

    def get_member(self, id):
        return next((m for m in self._members if m["id"] == id), None)

    def get_all_members(self):
        return self._members
