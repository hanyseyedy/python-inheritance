class Person:
    ClassAttribute = "test valeu"

    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age

    def ShowFullName(self):
        f"{self.name} {self.family}"

    @classmethod
    def ShowClassAttribute(cls):
        return Person.ClassAttribute

class User(Person):
    pass

hany = Person("hany", "seyedy", 37)
mohammad = User("mohammad", "seyedy", 12)

print(hany.name)

print(mohammad.name)

print(mohammad.ClassAttribute)

print(User.ClassAttribute)

print(User.ShowClassAttribute())