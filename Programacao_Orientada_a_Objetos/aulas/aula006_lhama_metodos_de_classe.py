class MinhaClasse:

    # atributo estático é um atributo de classe: isso significa que não está vinculado a nenhum objeto individualmente, mas sim à classe como um todo. -> o valor dele é unico tanto pra classe, quanto para objetos
    estatico = "lhama"

    def __init__(self, estado) -> None:
        # contexto de classe, nesse caso o atributo privado, só é acessado dentro da classe
        self.__estado = estado

    ## caso 1:
    # def print_variavel_de_classe(self):
    #     print(estatico)

    # # caso 2: -> o estatico que está aqui, não é o mesmo  do atributo estatico da classe
    # def print_variavel_de_classe(self):
    #     estatico = 3
    #     print(estatico)

    # caso 3:
    def print_variavel_de_classe(self):
        print(self.estatico)

    # caso 4: dá para alterar o atributo de classe esático? dentro do método? Será que repercurte para todos os objetos?
    def alteracao_da_variavel_de_classe(self):
        # como se fosse: objeto1.__estado = estado
        self.estatico = "Anterando dentro do método, mas com self só se aplica ao objeto que chamar esse método"


# contexto do objeto
objeto1 = MinhaClasse(True)
objeto2 = MinhaClasse(True)

# ERRO casso 1
# objeto1.print_variavel_de_classe()
# ERRO: NameError: name 'estatico' is not defined. Did you mean: 'self.estatico'?

# caso 2 - mas é diferente do que está na classe
objeto1.print_variavel_de_classe()  # output: 3

# caso 3
objeto1.print_variavel_de_classe()  # output: lhama

# caso 4
objeto1.print_variavel_de_classe()  # output: lhama
objeto1.alteracao_da_variavel_de_classe()
# só alterou o objeto1 -> foi feito igual ao espelho - da aula 5
print(
    objeto1.estatico
)  # output: "Anterando dentro do método, mas com self só se aplica ao objeto que chamar esse método"
print(objeto2.estatico)  # output:lhama
print(MinhaClasse.estatico)  # output:lhama

# CASO 5 @classmethod


class MinhaClasse:

    # atributo estático é um atributo de classe: isso significa que não está vinculado a nenhum objeto individualmente, mas sim à classe como um todo. -> o valor dele é unico tanto pra classe, quanto para objetos
    estatico = "lhama"

    def __init__(self, estado) -> None:
        # contexto de classe, nesse caso o atributo privado, só é acessado dentro da classe
        # como se fosse: MinhaClasse.__estado = estado
        self.__estado = estado

    def print_variavel_de_classe(self):
        print(self.estatico)

    # caso 5: troca o self para cls -> cls: acessando o cotexto geral da classe
    @classmethod  # método de classe
    def alteracao_da_variavel_de_classe(cls):
        cls.estatico = "Anterando atributo estático da classe, com cls dentro do método"


# contexto do objeto
objeto1 = MinhaClasse(True)
objeto2 = MinhaClasse(True)
objeto3 = MinhaClasse(True)

# agora que tem o @classmethod e cls a alteração é feita para todos
objeto1.alteracao_da_variavel_de_classe()
print(
    objeto1.estatico
)  # output: Anterando atributo estático da classe, com cls dentro do método
print(
    objeto2.estatico
)  # output: Anterando atributo estático da classe, com cls dentro do método
print(
    MinhaClasse.estatico
)  # output: Anterando atributo estático da classe, com cls dentro do método

print(
    objeto3.estatico
)  # output: Anterando atributo estático da classe, com cls dentro do método
