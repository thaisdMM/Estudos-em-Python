# Encapsulamento PROTEGIDO

# O encapsulamento protegido em Python é um conceito de convenção, não de imposição técnica.
# Python não possui palavras-chave como protected ou private para restringir o acesso.
# Uma variável ou método é considerado protegido quando seu nome começa com um único sublinhado (_).

# REGRA:

# Acesso Externo: Você não deve acessar diretamente membros protegidos (variáveis ou métodos) de fora da classe ou das classes filhas.

# Acesso Interno: Você pode acessar e usar esses membros dentro da classe em que foram definidos e em qualquer classe que herde dela (classe filha).


class Mamifero:
    def __init__(self, localizacao) -> None:
        self.localizacao = localizacao

    def andar(self) -> None:
        print(f"O animal está andandos pelo {self.localizacao}")

    # método protegido: acessível por classes mães e classes filhas
    def _dormir(self) -> None:
        print("O animal está dormindo.")


class Gato(Mamifero):
    def __init__(self, localizacao) -> None:
        super().__init__(localizacao)

    # método específico da classe Gato -> um objeto de Mamifero não acessa esse método específico da classe filha
    def miar(self) -> None:
        print("O gato está miando.")
        self._dormir()


# # Caso 1 método privado: __dormir -> primeiro exemplo __dormir era privado, agora vai trocar para protegido
# cat = Gato("Argentina")
# cat.miar()
# output: AttributeError: 'Gato' object has no attribute '_Gato__dormir'

# caso 3 _dormir -> metodo protegido
cat = Gato("Argentina")
cat.miar()

# caso 4 -> Deveria dar ERRO: elementos protegidos não são chamados por objetos, mas ainda é possível acessar
## Convenção em Python: não acessar elementos com _
cat._dormir()  # output: O animal está dormindo.

# Caso 5


class Mamifero:
    def __init__(self, localizacao) -> None:
        self.localizacao = localizacao
        # Caso 5
        self._tamanho = 1.23

    def andar(self) -> None:
        print(f"O animal está andandos pelo {self.localizacao}")

    # método protegido: acessível por classes mães e classes filhas
    def _dormir(self) -> None:
        print("O animal está dormindo.")


class Gato(Mamifero):
    def __init__(self, localizacao) -> None:
        super().__init__(localizacao)

    # método específico da classe Gato -> um objeto de Mamifero não acessa esse método específico da classe filha
    def miar(self) -> None:
        print("O gato está miando.")
        self._dormir()
        print(self._tamanho)


cat = Gato("Argentina")
cat.miar()
# ERRADO:
cat._dormir()  # elementos protegidos não são chamados por objeto
print(cat._tamanho)  # elementos protegidos não são chamados por objeto
