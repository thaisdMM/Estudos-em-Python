## INHERITANCE

# Herança é um mecanismo da Programação Orientada a Objetos que permite reutilizar código ao criar uma nova classe com base em uma classe existente. A classe nova (chamada classe filha, ou subclasse) herda os atributos e métodos da classe original (chamada classe pai, ou superclasse).

# A herança é usada para:

# Reutilizar código comum entre classes relacionadas.

# Promover organização e clareza em hierarquias lógicas (ex: Animal → Mamífero → Cachorro).

# Facilitar manutenção e expansão do sistema: alterações na superclasse refletem nas subclasses.

# Permitir generalização e especialização de comportamentos — você pode ter métodos padrão na superclasse e sobrescrevê-los (override) nas subclasses.

# Como funciona a herança em Python?
# Em Python, a herança é implícita e simples: uma subclasse herda tudo da superclasse e pode sobrescrever (redefinir) qualquer comportamento.

# Observações importantes sobre herança:
# Uma subclasse pode herdar de apenas uma classe (herança simples), ou de várias (herança múltipla), mas herança múltipla deve ser usada com cautela.

# É possível sobrescrever métodos da superclasse na subclasse.

# Você pode usar a função super() dentro da subclasse para chamar métodos da superclasse — útil, por exemplo, quando você quer ampliar um comportamento e não substituí-lo por completo.


# A car is a vehicle
# A bike is a vehicle


class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting.")

    def stop(self):
        print("Vehicle is stopping")


## subclasse
class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        # super refer a super class of car(Vehicle) ->chama o __init__ de Vehicle -> não precisa repetir os dados
        super().__init__(brand, model, year)

        # aqui está chamando os atributos especificos criados para class car
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels


## subclasse
class Bike(Vehicle):
    def __init__(self, brand, model, year, number_of_whels):

        super().__init__(brand, model, year)

        self.number_of_wheels = number_of_whels


car = Car("Ford", "Focus", 2008, 5, 4)

bike = Bike("Honda", "Scoopy", 2018, 2)

print(car.__dict__)  # print todos atributos do objeto com o .__dic__
## output: {'brand': 'Ford', 'model': 'Focus', 'year': 2008, 'number_of_doors': 5, 'number_of_wheels': 4}
print(bike.__dict__)
## output: {'brand': 'Honda', 'model': 'Scoopy', 'year': 2018, 'number_of_wheels': 2}
car.start()
bike.start()
