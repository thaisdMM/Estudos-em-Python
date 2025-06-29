class Pessoa:
    # metodo construtor
    def __init__(self, nome, altura, idade):
        # atributos:
        self.nome = nome
        self.altura = altura
        self.idade = idade

    # métodos
    def correr(self, km):
        print(f"Todos os dias eu corro {km}km.")

    def comer(self, comida):
        print(f"Eu amo comer: {comida}.")

#objeto : pessoa1 -> criei esse objeto a partir da instanciação de uma classe
pessoa1 = Pessoa("João", 1.80, 35)
print(f"Olá, meu nome é {pessoa1.nome}")
print(f"Eu tenho {pessoa1.altura:.2f} de altura e {pessoa1.idade} anos de idade.")
pessoa1.comer("Hambúrguer com batata frita e coca-cola.")
pessoa1.correr(10)


pessoa2 = Pessoa("Ana", 1.55, 28)
print(f"Olá, meu nome é {pessoa2.nome}")
print(f"Eu tenho {pessoa2.altura:.2f} de altura e {pessoa2.idade} anos de idade.")
pessoa2.comer("comidas saudáveis: salada é minha comida favorita")
pessoa2.correr(5)
