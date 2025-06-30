class Person:
    # method construtor
    def __init__(self, name, age):
        # atribute -data
        self.name = name
        self.age = age

    # method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# instanciou uma nova person object - cada pessoa é especifica,
person1 = Person("Lucas", 33)
person1.greet()

# instanciou uma nova person object - cada pessoa é especifica,
person2 = Person("Yara", 22)
person2.greet()
