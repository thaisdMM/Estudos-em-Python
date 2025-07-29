## POLYMORPHISM -> "having multiple forms"
## Poly = many + Morph = forms

# Na Programação Orientada a Objetos (POO), ele descreve a capacidade de objetos diferentes responderem ao mesmo método (ou operação) de maneiras diferentes.

# Como ele funciona?

# O polimorfismo pressupõe herança ou interfaces (abstrações). Ele se manifesta quando:

# Subclasses herdam de uma superclasse (ou implementam uma interface/abstração).
# Essas subclasses reescrevem métodos (override), adaptando o comportamento.
# Um código cliente (usuário da classe) trata objetos diferentes da mesma forma, chamando o mesmo método sem saber exatamente de que classe o objeto é.
# A chave: o mesmo nome de método, mas comportamentos diferentes, dependendo do objeto que o executa.

# Para que serve o polimorfismo?

# Generalizar o código, tornando-o mais flexível e extensível.
# Isolar o que varia, respeitando o princípio do aberto/fechado (OCP).
# Substituir comportamentos em tempo de execução, sem modificar o código cliente.
# Facilitar testes e manutenção, pois lida-se com interfaces em vez de implementações.

# 1- WITHDOW POLYMORPHISM


class Car:
    def __init__(self, brand, model, year, number_of_doors):
        self.brand = brand
        self.model = model
        self.year = year
        self.number_of_doors = number_of_doors

    def start(self):
        print("Car is starting.")

    def stop(self):
        print("Car is stopping")


class Motorcycle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_bike(self):
        print("Motorcycle is starting.")

    def stop_bike(self):
        print("Motorcycle is stopping")


# Create list of vehicles to inspect
vehicles = [Car("Ford", "Focus", 2009, 5), Motorcycle("Honda", "Scoopy", 2019)]

# Use polimorfismo para remover estruturas condicionais complexas (if, elif, else) como abaixo, substituindo por objetos com comportamentos especializados.

# Lop through list of vehicles and inspect them
for vehicle in vehicles:
    if isinstance(vehicle, Car):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    elif isinstance(vehicle, Motorcycle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start_bike()
        vehicle.stop_bike()
    else:
        raise Exception("Object is not a valid vehicle")

# # output:
# # Inspecting Ford Focus (Car)
# # Car is starting.
# # Car is stopping
# # Inspecting Honda Scoopy (Motorcycle)
# # Motorcycle is starting.
# # Motorcycle is stopping


##2- WITH POLYMORPHISM

## Criando uma superclass


class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting.")

    def stop(self):
        print("Vehicle is stoppig.")


## inheritance
class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    # Se comentar o codigo abaixo, ele da print no codigo geral de Vehicle,
    # senão comentar o codigo abaixo subscreve o codigo da class Vehicle
    def start(self):
        print("Car is starting.")

    def stop(self):
        print("Car is stopping")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    # Se comentar o codigo abaixo, ele da print no codigo geral de Vehicle,
    # senão comentar o codigo abaixo subscreve o codigo da class Vehicle -os métodos tem que ter o mesmo nome
    def start(self):
        print("Motorcycle is starting.")

    def stop(self):
        print("Motorcycle is stopping")


# Create list of vehicles to inspect
vehicles = [Car("Ford", "Focus", 2009, 5), Motorcycle("Honda", "Scoopy", 2019)]

for vehicle in vehicles:
    if isinstance(vehicle, Vehicle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    else:
        raise Exception("Object is not a valid vehicle")

## agora veiculo é uma lista e dá para reduzir a lógica anterior

# Create list of vehicles to inspect
vehicles: list[Vehicle] = [
    Car("Ford", "Focus", 2009, 5),
    Motorcycle("Honda", "Scoopy", 2019),
]

for vehicle in vehicles:
    print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
    vehicle.start()
    vehicle.stop()

# Adicionando uma nova classe sem ter que mexer tanto no código anterior,
# se tivesse condicional como no primeiro exemplo toda vez que adicionasse uma classe teria que mexer na condicional, ou acrescentar,


class Plane(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def start(self):
        print("Plane is starting.")

    def stop(self):
        print("Plane is stopping.")


vehicles: list[Vehicle] = [
    Car("Ford", "Focus", 2009, 5),
    Motorcycle("Honda", "Scoopy", 2019),
    Plane("Boeing", "747", 2015, 16),
]

for vehicle in vehicles:
    print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
    vehicle.start()
    vehicle.stop()
