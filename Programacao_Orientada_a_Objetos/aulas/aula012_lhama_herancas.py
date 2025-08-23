# HERANÇA

# a herança permite que uma nova classe, chamada de classe filha (ou subclasse), herde os atributos e métodos de uma classe existente, chamada de classe pai (ou superclasse).

# O principal objetivo da herança é promover a reutilização de código e estabelecer uma relação de "é um tipo de".
# -> ex: um Cachorro é um tipo de Mamifero.


class Mamifero:
    def __init__(self) -> None:
        self.localizao = "Brasil"

    def andar(self) -> None:
        print(f"O animal está andandos pelo {self.localizao}")


# Caso 2- adicionou classe Cachorro herdando Mamífero e não criou nehum atributo nem método, usou pass
class Cachorro(Mamifero):
    pass


# Caso 1 - objeto da superclasse Mamifero
mamifero = Mamifero()
mamifero.andar()
# Caso 2 - objeto da subclasse Cachorro
# mesmo sem ter métodos ou atributos, Cachorro(Mamifero) herda o comportamento que mamífero tem
bruxa = Cachorro()
bruxa.andar()
valor = bruxa.localizao
print(valor)


# caso 3 - colocando comportamento na classe Cachorro


class Mamifero:
    def __init__(self) -> None:
        self.localizao = "Brasil"

    def andar(self) -> None:
        print(f"O animal está andandos pelo {self.localizao}")


class Cachorro(Mamifero):
    def latir(self) -> None:
        print("O cachorro está latindo.")
        self.andar()


dog = Cachorro()
dog.latir()

# caso 4 - colocando variavel no metodo construtor da superclasse Mamifero


class Mamifero:
    def __init__(self, localizao) -> None:
        self.localizao = localizao

    def andar(self) -> None:
        print(f"O animal está andandos pelo {self.localizao}.")


class Cachorro(Mamifero):
    def __init__(self, localizao) -> None:
        # chama o init(construtor) da classe superior
        super().__init__(localizao)

    # método específico da classe Cachorro -> um objeto de Mamifero não acessa esse método específico da classe filha
    def latir(self) -> None:
        print("O cachorro está latindo.")
        self.andar()


# caso 5 - criando uma nova classe que também herda Mamifero


class Gato(Mamifero):
    def __init__(self, localizao) -> None:
        super().__init__(localizao)

    # método específico da classe Gato -> um objeto de Mamifero não acessa esse método específico da classe filha
    def miar(self) -> None:
        print("O gato está miando.")


# caso 4

# # agora dá erro se chamar sem a localizao
# dog = Cachorro()
# dog.latir()
# output: TypeError: __init__() missing 1 required positional argument: 'localizao'
# caso 4
dogzinho = Cachorro("Chile")
dogzinho.latir()

# caso 5

cat = Gato("Suíça")
cat.miar()
