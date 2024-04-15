class Person:
    def __init__(self, first_name, last_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.friends = [] 

    def name(self):
        return f"{self.first_name} {self.last_name}"

    def add_friend(self, person):
        if person not in self.friends:
            self.friends.append(person)

    def is_friend(self, person):
        if person in self.friends:
            return True
        return False

    def remove_friend(self, person):
        if person in self.friends:
            self.friends.remove(person)

    def __repr__(self):
        return self.name()

    def __eq__(self, other):

        if (
                self.first_name == other.first_name
                and self.last_name == other.last_name
                and self.phone == other.phone
                ):
            return True
        return False
