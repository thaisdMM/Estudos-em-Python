from abc import ABC, abstractmethod


# classe abstrata não possui objeto - so pode ser mae(heranca)
class Pessoa(ABC):
    def correr(self):
        print("A pessoa esta correndo de manha.")

    # obrigatorio: classe filha deve criar o metodo trabalhar
    @abstractmethod
    def trabalhar(self):
        pass


# # da erro: TypeError: Can't instantiate abstract class Pessoa with abstract method trabalhar
# p1 = Pessoa()
# p1.correr()


# todos que herdam da classe abstrata tem que implementar o @abstractmethod
class Professor(Pessoa):
    def trabalhar(self):
        print("O professor esta dando aula.")


class Cozinheiro(Pessoa):
    def trabalhar(self):
        print("O conzinheiro está cozinhando.")


p1 = Professor()
p1.trabalhar()
p1.correr()

p2 = Cozinheiro()
p2.trabalhar()
p2.correr()
