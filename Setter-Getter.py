class Person:

    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self._age = age

    # getter
    @property
    def age(self):
        return self._age

    # setter
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age not be negative!")
        
    @property
    def show_full_name_prop(self):
        return f"{self.name} {self.family}"

    def show_full_name(self):
        return f"{self.name} {self.family}"


me = Person("ali", "milady", 24)

print(me.name)

print(me.family)

print(me.age)
# me.age = -10
me.age = 33
print(me.age)

print(me.show_full_name())
print(me.show_full_name_prop)