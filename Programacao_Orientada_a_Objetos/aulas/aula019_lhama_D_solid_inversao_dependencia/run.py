from elementos.interfaces.elemento_interface import ElementoInterface
from elementos.elemento import Elemento
from elementos.elemento2 import Elemento2

# EXEMPLO 1- Dependencia muito forte
# class Principal:
#     def __init__(self) -> None:
#         # essa dependencia aqui é muito "dura"/total da classe principal com a classe elemento
#         self.__elemento = Elemento()

#     def run(self) -> None:
#         self.__elemento.executar()
#         print("Estou finalizando na classe Principal.")

# cl1 = Principal()
# cl1.run()


###
# EXEMPLO 2
# Principio da Inversão da Depência

# Colocar a interface no construtor facilita a inversão da dependência
# Torna a classe bem maleavel


class Principal:
    # declara que elemento é objeto da classe ElementoInterface
    def __init__(self, elemento: ElementoInterface) -> None:
        self.__elemento = elemento

    def run(self) -> None:
        self.__elemento.executar()
        print("Estou finalizando na classe Principal.")


# cria o objeto elemento
elem = Elemento()
elem2 = Elemento2()

# associa o objeto elemento na classe principal
cl2 = Principal(elem)
cl2.run()
cl3 = Principal(elem2)
cl3.run()
