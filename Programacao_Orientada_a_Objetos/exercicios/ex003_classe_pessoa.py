class Pessoa:
    # método construtor
    def __init__(self, nome, idade):
        # atributos
        self.nome = nome
        self.idade = idade

    # método
    def falar(self):
        return (
            f"Olá, meu nome é {self.nome}, eu tenho {self.idade}, prazer em conhecê-lo!"
        )


Jose = Pessoa("José", 55)
apresentacao1 = Jose.falar()
print(apresentacao1)
Maria = Pessoa("Maria", 33)
apresentacao2 = Maria.falar()
print(apresentacao2)
