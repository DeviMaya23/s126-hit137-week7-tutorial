class Person:
    """
    A class for a person.
    """
    def getGender(self):
        """
        To be implemented by subclasses.
        """
        pass


class Male(Person):
    def getGender(self):
        return "Male"


class Female(Person):
    def getGender(self):
        return "Female"


john = Male()
jane = Female()

print(john.getGender())
print(jane.getGender())
