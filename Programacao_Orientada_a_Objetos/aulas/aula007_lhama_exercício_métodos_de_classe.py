class Loja:
    # atributo estático de classe
    taxa = 1.15

    def __init__(self, valor: float) -> None:
        self.valor_produto_bruto = valor

    def consultar_valor_do_produto(self):
        valor_do_protuto = self.valor_produto_bruto * self.taxa
        print(f"valor do produto: {valor_do_protuto}")

    # método estático de classe
    @classmethod
    def editar_taxa_do_produto(cls, valor: float):
        cls.taxa = valor


loja_praia = Loja(30.50)
loja_shopping = Loja(10.39)
loja_rua = Loja(20.33)

loja_praia.consultar_valor_do_produto()  # output: valor do produto: 35.074999999999996
loja_shopping.consultar_valor_do_produto()  # output: valor do produto: 11.9485
loja_rua.consultar_valor_do_produto()  # output: valor do produto: 23.379499999999997

loja_rua.editar_taxa_do_produto(1.35)
print("Editei a taxa para 1.35. Alteração com @classmethod serve para todos")

loja_praia.consultar_valor_do_produto()  # output: valor do produto: 41.175000000000004
loja_shopping.consultar_valor_do_produto()  # output: valor do produto: 14.026500000000002
loja_rua.consultar_valor_do_produto()  # output: valor do produto: 27.4455
