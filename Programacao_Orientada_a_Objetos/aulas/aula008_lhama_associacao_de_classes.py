# Associação Simples:
## Associação: É um termo geral que descreve qualquer relacionamento onde um objeto usa outro.
# # Um objeto da classe Pessoa interage com um objeto da classe Interruptor passando-o como argumento para um método.


class Interruptor:
    def __init__(self, comodo: str) -> None:
        self.comodo = comodo

    def acender(self) -> None:
        print(f"Estou acendendo a luz do comodo: {self.comodo}")

    def apagar(self) -> None:
        print(f"Estou apagando a luz do comodo: {self.comodo}")


class Pessoa:
    # interruptor é to tipo Interruptor(classe)
    # associação simples: colocar uma clase no método de outra classe
    def acender_luzes(self, interruptor: Interruptor) -> None:
        interruptor.acender()

    def apagar_luzes(self, interruptor: Interruptor) -> None:
        interruptor.apagar()

    def dormir(self) -> None:
        print("A pessoa foi dormir.")


Marcos = Pessoa()
interuptor_sala = Interruptor("sala")
interruptor_quarto = Interruptor("quarto")
Marcos.acender_luzes(interuptor_sala)
Marcos.apagar_luzes(interruptor_quarto)
