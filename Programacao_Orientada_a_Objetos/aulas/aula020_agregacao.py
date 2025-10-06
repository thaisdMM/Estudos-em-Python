# A Agregação é um tipo de relacionamento de associação "Tem Um" (em inglês, Has-a) entre duas classes,
#  onde uma classe contém ou utiliza instâncias de outra classe.

# Características Chave da Agregação:
# Dependência Fraca (ou Relação de "Vida Independente"): O ponto mais importante da agregação é que as classes envolvidas podem existir e ter significado de forma independente. Se o objeto que contém for destruído, os objetos que são contidos (agregados) continuam a existir e podem ser reutilizados em outro contexto.

# Referência a Objetos Externos: A classe agregadora (a que contém) armazena referências aos objetos da classe agregada (a que é contida).


class Produto:
    def __init__(self, nome: str, valor: int) -> None:
        self.__nome = nome
        self.__valor = valor

    def informacoes_do_produto(self) -> None:
        print(f"Produto: {self.__nome} - Valor: {self.__valor}")


# O CarrinhoDeCompras apenas agrega/reúne os objetos Produto,
#  mas não é o responsável pela criação nem pela existência deles.
class CarrinhoDeCompras:
    def __init__(self) -> None:
        # 1. O Carrinho "TEM UMA" lista de Produtos
        self.__produtos = []

    def adicionar_produto(self, produto: Produto) -> None:
        # 2. O método recebe um objeto 'Produto'
        #    que já foi criado *externamente* e o adiciona à sua lista interna.
        self.__produtos.append(produto)

    def finalizar_compra(self) -> None:
        print("Compra finalizada.")
        print("  Produtos:   ")
        for product in self.__produtos:
            product.informacoes_do_produto()


# criou objetos da classe Produto
banana = Produto("banana", 3)  # O objeto 'banana' é criado *fora* do Carrinho.
pera = Produto("pera", 2)
uva = Produto("uva", 4)
# Se destruir a instância carrinho (por exemplo, del carrinho),
# os objetos banana, pera e uva ainda existiriam na memória e
# poderiam ser adicionados a outro carrinho de compras (carrinho2 = CarrinhoDeCompras())
# ou usados de outras formas no programa.

carrinho = CarrinhoDeCompras()
carrinho.adicionar_produto(banana)
carrinho.adicionar_produto(pera)
carrinho.adicionar_produto(uva)
carrinho.finalizar_compra()
