# O Princípio de Substituição de Liskov (LSP)

# uma classe filha (subtipo) deve ser capaz de ser usada no lugar de sua classe pai (super tipo) sem causar comportamentos inesperados, erros ou exceções.
# 2. Para que serve?
# O LSP serve para garantir a integridade do seu sistema. Quando ele é respeitado, o código se torna:

# Robusto: Você pode estender o sistema adicionando novas classes sem medo de quebrar o código existente. O seu código que usa a classe pai continuará funcionando com as classes filhas.

# Manutenível: Alterar o comportamento de uma classe filha não afeta o comportamento esperado das classes pai ou de outras classes filhas, desde que o contrato da classe pai seja mantido.

# Reutilizável: A herança se torna uma ferramenta poderosa para a construção de hierarquias de classes coesas, onde a lógica da classe pai pode ser reutilizada e estendida de forma segura.


# 1. Exemplo de Quebra do princípio de LISKOV


class Animal:
    def alimentar(self) -> None:
        print("O animal está se alimentando")


class Cachorro(Animal):
    def latir(self):
        print("O cachorro está latindo.")


# quebra do princípio de Liskov - comportamento diferente entre classe mãe e filha
class Peixe(Cachorro):
    def nadar(self):
        print("O peixe está nadando.")

    # o comportamento de cachorro era um print, aqui abaixo é um erro
    # a quebra do LSP: um objeto Peixe não pode ser substituído por um Cachorro sem quebrar a corretude do programa.
    def latir(self):
        raise Exception("Peixe não late")


def verificar_animal(animal: any):
    animal.alimentar()


def verificar_animal2(animal: any):
    animal.latir()


obj1 = Animal()
obj2 = Cachorro()
obj3 = Peixe()
verificar_animal(obj3)  # output: O animal está se alimentando
# erro da quebra do princípio de Liskov
verificar_animal2(obj3)  # output: Exception: Peixe não late

# 2. Exemplo correto

# Hierarquia de Herança Correta: A estrutura Salmao -> Peixe -> Animal é logicamente consistente. Um salmão é um peixe, e um peixe é um animal.

# Contrato de Comportamento: A classe Salmao não introduz nenhum comportamento inesperado nem sobrescreve métodos de forma que quebre o contrato de suas superclasses (Peixe e Animal). Ele herda os métodos alimentar() e nadar() sem alterá-los.


class Animal:
    def alimentar(self) -> None:
        print("O animal está se alimentando")


class Cachorro(Animal):
    def latir(self):
        print("O cachorro está latindo.")


class Peixe(Animal):
    def nadar(self):
        print("O peixe está nadando.")


# LSP: um subtipo (Salmao) pode ser substituído por seus supertipos (Peixe e Animal) sem quebrar o programa.
class Salmao(Peixe):
    pass


def verificar_animal(animal: any):
    animal.alimentar()


def verificar_animal2(animal: any):
    animal.nadar()


obj1 = Peixe()
obj2 = Cachorro()
obj3 = Salmao()
# Salmao possui o método alimentar() herdado de Animal.
verificar_animal(obj3)  # output: O animal está se alimentando
# Salmao herda o método nadar() de Peixe.
verificar_animal2(obj3)  # output: O peixe está nadando.
