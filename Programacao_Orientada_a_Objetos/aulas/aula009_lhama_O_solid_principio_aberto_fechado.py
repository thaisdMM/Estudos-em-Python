# princípio aberto/fechado - O - SOLID - Open/Closed Principle (OCP)

## Aberto: para extensão - Fechado: para modificação(código-fonte)

# Abertos para extensão: Isso significa que o comportamento de um módulo pode ser estendido ou modificado para atender a novas funcionalidades.

# Fechados para modificação: Isso significa que, uma vez que um módulo esteja pronto, seu código-fonte não deve ser alterado para adicionar novas funcionalidades.
## para adicionar uma nova funcionalidade, você deve criar um novo código, e não alterar um código já existente e funcionando.

## O objetivo principal é tornar o código mais robusto, fácil de manter e de evoluir, evitando o risco de quebrar funcionalidades existentes ao adicionar novas.

# 1- Esse primeiro exemplo está quebrando o princípio Aberto e Fechado, pois toda hora tem que alterar a classe Circo para colocar uma nova funcionalidade


class Circo:
    def apresentar(self, command: int) -> None:
        if command == 1:
            self.__show_palhaco()
        if command == 2:
            self.__show_malabarista()

        # 2 Quebra o OCP: Para adicionar um novo show você precisa modificar a classe Circo existente

        if command == 3:
            self.__show_magico()

    def __show_palhaco(self):
        print("O Palhaço está apresentando seu show.")

    def __show_malabarista(self):
        print("O Malabarista está apresentando seu show.")

    # 2
    # teve que criar mais um método para outro show e acrescentar mais um if
    def __show_magico(self):
        print("O Mágico está apresentando seu show.")


circo = Circo()
command = 1
circo.apresentar(command)

command = 3
circo.apresentar(command)

## 2- Usando o princípio Aberto e Fechado de SOLID - O


class Artista:
    def __init__(self, tipo: str) -> None:
        self.tipo = tipo

    def apresentar_show(self) -> None:
        print(f"O {self.tipo} está apresentando seu show!")


## Aplicando OCP: A classe Circo agora está "FECHADA" para modificação
class Circo:
    def apresentar(self, artista: Artista) -> None:
        print("O Circo está começando as apresentações.")
        artista.apresentar_show()
        print("O público aplaude!")


circo = Circo()
palhaco = Artista("palhaçoo")
magico = Artista("mágico")


## Você pode ESTENDER o sistema:
##->  simplesmente criando uma nova instância de Artista com um tipo diferente, sem precisar tocar no código da classe Circo
malabarista = Artista("malabarista")


circo.apresentar(palhaco)
circo.apresentar(magico)
circo.apresentar(malabarista)
