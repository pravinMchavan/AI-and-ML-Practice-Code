# Use a constructor (__init__) to initialize attributes and print them.

class check:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = check("pravin", 25)
p2 = check("kiran", 26)

print(p1.name)
print(p1.age)

print(p2.name)
print(p2.age)
        