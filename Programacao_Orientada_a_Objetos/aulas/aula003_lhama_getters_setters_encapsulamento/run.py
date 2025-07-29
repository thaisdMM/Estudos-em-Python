## GETTERS E SETTERS

class MinhaClasse:
    def __init__(self) -> None:
        # # privado
        # self.__valor = None
        # troca privado para publico
        self.valor = None

my_class = MinhaClasse()
my_class.valor = 3 ## Ferindo encapsulamento, porque o atributo tinha sido definido como privado
print(my_class.valor)


class MinhaClasse:
    def __init__(self) -> None:
        # atributo privado
        self.__valor = None
        self.__elemento = None

    # método setter - público, mas interage com um atributo privado
    # está usando typing: type hints tipando int None...
    def setter_valor(self, valor: int) -> None:
        self.__valor = valor

    # método getter - público, mas interage com um atributo privado
    def getter_valor(self) -> int:
        return self.__valor


my_class = MinhaClasse()
my_class.setter_valor(42)
valor = my_class.getter_valor()
print(valor)
