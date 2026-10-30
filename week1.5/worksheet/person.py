# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    def __init__(self, name, birth):
        """
        Creates a Person, given a name (non-empty string) and a date of
        birth (a date object).
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if name == "":
            raise ValueError("name must not be an empty string")
        if not isinstance(birth, date):
            raise TypeError("birth must be a date object")
        self.name = name
        self.birth = birth

    def initials(self):
        """
        Returns the uppercased initial letters of each part of the
        person's name, joined into a single string.
        """
        return "".join(part[0].upper() for part in self.name.split())

    def is_birthday(self):
        """
        Returns True if today is the person's birthday, False otherwise.
        """
        today = date.today()
        return (today.month, today.day) == (self.birth.month, self.birth.day)