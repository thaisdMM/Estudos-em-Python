# ## Exercício 3: Subindo o Nível com Herança e Polimorfismo

# **Objetivo:** Criar uma estrutura de classes que modela diferentes tipos de veículos e demonstre o Polimorfismo.

# **Problema:** Desenvolva um sistema de classes para veículos.

# 1.  **Classe Base (`Veiculo`):**
# 2.  **Classes Derivadas (Filhas):**
# 3.  **Teste de Polimorfismo:**

# Vantagem: O uso do __str__ (e seu primo __repr__, para representações de desenvolvedor/depuração) é o padrão esperado em Python.
# Em vez de criar um método com nome arbitrário (show_detail), você usa a interface que o core da linguagem espera, tornando seu código mais previsível e mais fácil de ser integrado em frameworks.


class Vehicle:
    def __init__(self, brand: str, model: str, year: int):
        self._brand = brand
        self._model = model
        self._year = year

    def get_brand(self) -> str:
        return self._brand

    def get_model(self) -> str:
        return self._model

    def get_year(self) -> int:
        return self._year

    def accelerate(self):
        raise NotImplementedError("The accelerate method must be implemented!")

    def show_detail(self) -> str:
        return f"Vehicle: {self.get_brand()} | model: {self.get_model()} | year: {self.get_year()}"

    # O método mágico __str__
    def __str__(self) -> str:
        """
        Retorna uma representação amigável do veículo.
        Substitui seu método show_detail().
        """
        # Note que aqui eu estou acessando os atributos encapsulados (o que é permitido
        # dentro da própria classe) para construir a string.
        return f"Vehicle: {self._brand} | Model: {self._model} | Year: {self._year}"


class Car(Vehicle):
    def __init__(self, brand: str, model: str, year: int):
        super().__init__(brand, model, year)

    def accelerate(self):
        return "The car is accelerating smoothly!"

    def wheels(self):
        return "The car is a vehicle with 4 wheels."


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    def accelerate(self):
        return f"The motorcycle is accelerating quickly!!!"

    def helmet(self):
        return f"A helmet is mandatory for motorcycles."


corsa = Car("Chevrolet", "Corsa", 2010)
print(corsa.show_detail())
print(corsa.accelerate())
print(corsa.wheels())

harley = Motorcycle("Harley-Davidson", "Street Bob", 2023)
print()
print(harley.show_detail())
print(harley.accelerate())
print(harley.helmet())

vehicles = [
    Car("Volkswagen", "Gol", 2017),
    Motorcycle("Suzuki", "Katana", 2000),
    Car("Ford", "Focus", 2009),
    Motorcycle("Honda", "Scoopy", 2019),
]
print()
for vehicle in vehicles:
    if isinstance(vehicle, Vehicle):
        print(
            f"Inspecting {vehicle.get_brand()} | {vehicle.get_model()} | {vehicle.get_year()}|({type(vehicle).__name__})"
        )
        print(vehicle.accelerate())
        print()

    else:
        raise Exception("Object is not a valid vahicle.")


# --- Teste __str__---
onix = Vehicle("Chevrolet", "Onix", 2020)

# 1. Quando você chama o print(), ele usa o __str__
print(onix)  # Saída: Vehicle: Chevrolet | Model: Onix | Year: 2020
