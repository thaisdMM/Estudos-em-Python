from abc import ABC, abstractmethod

# para fazer Interface utliza classes abstratadas com metrodos abastratos


# Essa classe é uma interface: ela é abstrata e é composta somente por metodos abastratos
# assinatura do que você quer que implemente na classe
class Trabalhador(ABC):

    @abstractmethod
    def trabalhar(self) -> None:
        pass

    @abstractmethod
    def ir_para_casa(self) -> None:
        pass

    @abstractmethod
    def horario_de_almoco(self) -> None:
        pass


# tem que implentar todos os metodos da interface
# implementação concreta da interface
class Professor(Trabalhador):

    def trabalhar(self) -> None:
        print("O professor esta trabalhando.")

    def ir_para_casa(self):
        print("O professor esta indo para casa")

    def horario_de_almoco(self):
        print("O professor esta almocando.")


class Engenheiro(Trabalhador):

    def trabalhar(self) -> None:
        print("O engenheiro esta trabalhando.")

    def ir_para_casa(self):
        print("O engenheiro esta indo para casa")

    def horario_de_almoco(self):
        print("O engenheiro esta almocando.")


# função
# tipou trabalhador com a interface,
# não precisa ser o professor, pode ser qualquer uma das classes que implementam a interface trabalhador
def comunicar_o_trabalhador(trabalhador: Trabalhador):
    trabalhador.trabalhar()
    print("Comunicar o trabalhador para ir para casa")
    trabalhador.ir_para_casa()


p1 = Professor()
p2 = Engenheiro()

comunicar_o_trabalhador(p1)
print()
comunicar_o_trabalhador(p2)
