class Animal:
    # método construtor
    def __init__(self, name, species, age):
        # atributos
        self.name = name
        self.species = species
        self.age = age

    # métodos
    def fazer_som(self, som):
        print(som)

    def eh_friendly(self):
        answer = (
            input("Is friendly? Enter: T to true or F to false: ").strip().upper()[0]
        )
        if answer == "T":
            print("It is my best friend.")
            return True
        else:
            print("Wild animal. UHHHH!!!")
            return False

    def envelhecer(self):
        # alteração do estado de um objeto em Python
        # isso altera o estado interno do objeto.
        # Ou seja: o objeto agora "tem memória da mudança".
        self.age = self.age + 1
        print(f"age: {self.age}")


animal1 = Animal("Maumau", "cat", 3)
print("Animal data:")
print(f"name: {animal1.name}")
print(f"species: {animal1.species}")
animal1.fazer_som("miau... miau")
animal1.envelhecer()
friendly = animal1.eh_friendly()
if friendly:
    print("I love it!")
else:
    print("I'm afraid!")

animal2 = Animal("Angry", "tigre", 6)
print("Animal data:")
print(f"name: {animal2.name}")
print(f"species: {animal2.species}")
animal2.fazer_som("ROAAARRR!!!")
animal2.envelhecer()
friendly = animal2.eh_friendly()
if friendly:
    print("I love it!")
else:
    print("I'm afraid!")
