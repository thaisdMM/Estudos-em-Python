# Polimorfismo


# o polimorfismo é um princípio que permite que objetos de diferentes classes, que compartilham a mesma interface ou herdam de uma classe base comum, sejam tratados por meio dessa interface comum.

# O polimorfismo é uma ferramenta poderosa que nos permite escrever código que se adapta a novos tipos de dados ou objetos sem precisar de modificações extensas. Ele promove a reutilização de código e a manutenção mais simples, tornando-o essencial para a construção de sistemas robustos.

# Existem dois tipos principais de polimorfismo em Python:

# Polimorfismo de Sobrescrita (Overriding): Acontece quando uma classe filha redefine um método que já foi definido na classe pai.

# Polimorfismo de Inclusão (Inclusion): É o tipo mais comum e se refere ao fato de que um objeto de uma classe filha pode ser usado em qualquer lugar onde um objeto da classe pai seja esperado.


class ClasseQualquer:
    def fazer(self) -> None:
        print("Estou fazendo algo.")


class OutraCoisa(ClasseQualquer):
    def preparar(self) -> None:
        print("Estou preparando algo.")

    # Caso 2 - implementando o metodo fazer: sobscreve o método de cima

    def fazer(self) -> None:
        print("Estou fazendo outra coisa.")


objeto1 = ClasseQualquer()
objeto2 = OutraCoisa()

# # caso 1 - não tinha o metodo fazer na classe OutraCoisa
# objeto1.fazer() # output: Estou fazendo algo.
# objeto2.fazer() # output: Estou fazendo algo.

# caso 2 - método fazer implementado na classe OutraCoisa

objeto1.fazer()  # output: Estou fazendo algo.
objeto2.fazer()  # output: Estou fazendo outra coisa.

# Caso 3 - retirou o método da classe filha e criou uma função

# Caso 3 - Atribuição Dinâmica de Funções

# Não é um exemplo de polimorfismo de sobrescrita, mas sim de uma característica de Python: a capacidade de tratar funções como objetos e atribuí-las a atributos de classes dinamicamente.
# não é considerado uma boa prática para alcançar o polimorfismo, pois pode levar a um código difícil de rastrear e manter


class ClasseQualquer:
    def fazer(self) -> None:
        print("Estou fazendo algo.")


class OutraCoisa(ClasseQualquer):
    def preparar(self) -> None:
        print("Estou preparando algo.")


def fazer_funcao() -> None:
    print("Estou fazendo outra coisa.")


objeto1 = ClasseQualquer()
objeto2 = OutraCoisa()
# atribuindo o valor da função, mesmo chamando como metodo fazer abaixo, o valor vai ser alterado para o valor da função
objeto2.fazer = fazer_funcao

objeto1.fazer()  # output: Estou fazendo algo.
objeto2.fazer()  # output: Estou fazendo outra coisa.
