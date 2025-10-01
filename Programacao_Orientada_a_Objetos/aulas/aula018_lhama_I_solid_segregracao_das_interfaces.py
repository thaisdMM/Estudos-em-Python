from abc import ABC, abstractmethod

# I - SOLID - Segregação das Interfaces
# > Não tem que depender de uma interface se nao a utilizo completamente


# Interface
class Trabalhador(ABC):

    @abstractmethod
    def trabalhar(self) -> None:
        pass

    @abstractmethod
    def ir_para_casa(self) -> None:
        pass

    @abstractmethod
    def consultar_beneficio(self) -> None:
        pass


# Essa classe não tem problemas com a interface
# tem que implentar todos os metodos da interface
# implementação concreta da interface
class Professor(Trabalhador):

    def trabalhar(self) -> None:
        print("O professor esta trabalhando.")

    def ir_para_casa(self) -> None:
        print("O professor esta indo para casa")

    def consultar_beneficio(self) -> None:
        print("Consultando beneficios da CLT.")


# CASO 1- QUEBRA DA SEGREGAÇÃO DAS INTERFACES

# O PROBLEMA é Essa classe abaixo, ela tem problemas com a interface
# tem que implentar todos os metodos da interface, mas nesse caso não dá
# Essa classe teria que ter outra interface para ela,
# pois ela quebra o principio da segregração das interfaces, ele depende de uma interface que ele não vai utilizar completamente


class ProfessorSubstituto(Trabalhador):

    def trabalhar(self) -> None:
        print("O professor substituto esta trabalhando.")

    def ir_para_casa(self) -> None:
        print("O professor substituto esta indo para casa")


# DÁ ERRO
# TypeError: Can't instantiate abstract class ProfessorSubstituto with abstract method consultar_beneficio
# p2 = ProfessorSubstituto()

# # CASO 2 - APLICAÇÃO DA SEGREGAÇÃO DAS INTERFACES


# Interface
class Trabalhador(ABC):

    @abstractmethod
    def trabalhar(self) -> None:
        pass

    @abstractmethod
    def ir_para_casa(self) -> None:
        pass

    @abstractmethod
    def consultar_beneficio(self) -> None:
        pass


# Cria uma nova interface que corresponde com ProfessorSubstituto
class TrabalhadorTemporario(ABC):

    @abstractmethod
    def trabalhar(self) -> None:
        pass

    @abstractmethod
    def ir_para_casa(self) -> None:
        pass


class Professor(Trabalhador):

    def trabalhar(self) -> None:
        print("O professor esta trabalhando.")

    def ir_para_casa(self) -> None:
        print("O professor esta indo para casa")

    def consultar_beneficio(self) -> None:
        print("Consultando beneficios da CLT.")


class ProfessorSubstituto(TrabalhadorTemporario):

    def trabalhar(self) -> None:
        print("O professor substituto esta trabalhando.")

    def ir_para_casa(self) -> None:
        print("O professor substituto esta indo para casa")


p3 = ProfessorSubstituto()
p3.trabalhar()
p3.ir_para_casa()
