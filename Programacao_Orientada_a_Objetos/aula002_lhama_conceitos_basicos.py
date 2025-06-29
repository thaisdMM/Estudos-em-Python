class MinhaClasse:
    # método da clase, parecido com função
    # self se refere a classe, o método está dentro da classe
    def metodo_1(self):
        print("minha ação 1")
        print("minha ação 2")
        return "Olá Mundo"


# objeto         #classe -> a partir da classe instanciamos um objeto
minha_classe = MinhaClasse()

# a classe por si só não realiza a ação, quem realiza é o objeto da classe

# minha_classe.metodo_1()# nao precisa colocar paremetro dentro, pois o self já se refere a classe

# retorno do método:
response = minha_classe.metodo_1()
print(response)
# # output:
# minha ação 1
# minha ação 2
# Olá Mundo

# atributo: são características da classe


class MinhaClasse:
    # método construtor - vai constuir os atributos através dele
    # o método construtor é o primeiro método a ser executado, antes de todos os outros
    def __init__(self, info):
        # print("Estou no construtor!")
        ## definindo atributos(características na classe)
        self.atributo1 = "meu atributo"
        self.atributo2 = [1, 2, "a"]  # pode ser muitas coisas, listas, numeros...
        ## ele também pode ser definido a partir da entrada de dados no construtor -
        # >> nesse momento acrescentou info após o self no __init__
        self.new_atribute = info
        print(self.new_atribute)

    def metodo_1(self):
        print("Minha ação 1")
        print("Minha ação 2")
        print(self.atributo2)
        return "Olá Mundo"


# Mesmo sem chamar método nenhum deixando a classe instansciada, ele roda o método construtor
# minha_classe = MinhaClasse()

## Após acrescentar a info no construtor
minha_classe = MinhaClasse("info aqui no construtor")


response = minha_classe.metodo_1()
print(response)

# agora chamando a classe ele roda o método construtor primeiro e depois os outros
response = minha_classe.metodo_1()
print(response)
# output:
# Estou no construtor!
# Minha ação 1
# Minha ação 2
# Olá Mundo

# após acrescentar a info e os atributos e mudar um pouco o código o resultado do output é outro:
response = minha_classe.metodo_1()
print(response)

# output:
# info aqui no construtor
# Minha ação 1
# Minha ação 2
# [1, 2, 'a']
# Olá Mundo


class MinhaClasse:
    # método construtor - vai constuir os atributos através dele
    # o método construtor é o primeiro método a ser executado, antes de todos os outros
    def __init__(self, info, elem):
        # print("Estou no construtor!")
        ## definindo atributos(características na classe)
        self.atributo1 = "meu atributo"
        self.atributo2 = elem  # pode ser muitas coisas, listas, numeros...
        ## ele também pode ser definido a partir da entrada de dados no construtor -
        # >> nesse momento acrescentou info após o self no __init__
        self.atributo3 = [1, 2, "a"]
        self.new_atribute = info
        print(self.new_atribute)

    # você pode colocar os atributos dentro dos métodos
    def metodo_1(self):
        print("Minha ação 1")
        print("Minha ação 2")
        print(self.atributo2)
        print(self.atributo3)
        return "Olá Mundo"

    # sempre usar o self para falar que está dentro daquela classe
    def metodo_2(self, numero):
        print(
            self.atributo3[1] + numero
        )  # [1, 2, 'a'] >> pegou o elemento 1 da lista: 2 e vai somar com numero


# Mesmo sem chamar método nenhum deixando a classe instansciada, ele roda o método construtor
# minha_classe = MinhaClasse()

## Após acrescentar a info no construtor
minha_classe = MinhaClasse("info aqui no construtor", 213)

response = minha_classe.metodo_1()
print(response)

minha_classe.metodo_2(3)
# o número 3 foi passado para ser somado com o elemento 1 da lista
# 2 + 3 = 5


# pode chamar um método dentro de outro método:


class MinhaClasse:
    def __init__(self, info, elem):
        self.atributo1 = "meu atributo"
        self.atributo2 = elem
        self.atributo3 = [1, 2, "a"]
        self.new_atribute = info
        print(self.new_atribute)

    # você pode colocar os atributos dentro dos métodos
    def metodo_1(self):
        print("Minha ação 1")
        print("Minha ação 2")
        print(self.atributo2)
        return "Olá Mundo"

    # pde chamar um método dentro de outro método
    def metodo_2(self, numero):
        self.metodo_1()
        print(self.atributo3[1] + numero)


minha_classe = MinhaClasse("info aqui no construtor", 213)

# response = minha_classe.metodo_1()
# print(response)

minha_classe.metodo_2(3)
# output
# info aqui no construtor
# Minha ação 1
# Minha ação 2
# 213
# 5
