# Create a class with attributes name and age, then create an object and print its attributes.

class person:

    def __init__(self, name, age):

        self.name = name
        self.age = age

person1 = person("pravin", 25)

print("Name -", person1.name)
print("age- ", person1.age)