# Método privado


class Pessoa:
    def __init__(self, altura, cpf) -> None:
        self.altura = altura
        # self.cpf = cpf

    ## na mesma classe - acessando o método privado:
    def apresentar(self):
        print(f"Olá! Minha altura é: {self.altura}")
        self.__coletar_documento()

    # método privado - só acessado na própria classe
    def __coletar_documento(self):
        print(f"Meu documento - {self.cpf}")


jorge = Pessoa("1.90", "000.000.000-00")
# ERRO - método privado não pode ser acessado fora da classe
# jorge.__coletar_documento()
# output: AttributeError: 'Pessoa' object has no attribute '__coletar_documento'
jorge.apresentar()


class Pessoa:
    def __init__(self, altura, cpf) -> None:
        self.altura = altura
        ## Atributo privado
        self.__cpf = cpf

    ## na mesma classe - acessando o método privado:
    def apresentar(self):
        print(f"Olá! Minha altura é: {self.altura}")
        self.__coletar_documento()

    # método privado - só acessado na própria classe
    def __coletar_documento(self):
        print(f"Meu documento - {self.__cpf}")


# É Possível acessar o atributo privado, fora da classe, mas NÃO DEVE SER FEITO, NÃO É RECOMENDADO
jorge = Pessoa("1.90", "000.000.000-00")
jorge.__cpf = "123abc"
print(jorge.__cpf)
jorge.apresentar()
# output: - aparece o CPF trocado, depois o cpf antigo
# 123abc
# Olá! Minha altura é: 1.90
# Meu documento - 000.000.000-00
