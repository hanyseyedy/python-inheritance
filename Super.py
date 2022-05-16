class Person:
    def __init__(self, name, family):
        self.name = name
        self.family = family

    @property
    def ShowFullName(self):
        return f"{self.name} {self.family}"

class User(Person):
    def __init__(self, name, family, email):
        super().__init__(name, family)
        self.email = email

hany = Person("hany", "seyedy")
mohammad = User("mohammad", "seedy", "test@test.com")

print(hany.ShowFullName)

print(mohammad.email)
print(mohammad.ShowFullName)
