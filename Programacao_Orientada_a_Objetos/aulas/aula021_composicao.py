# COMPOSIÇÃO - Compor uma classe através de outra classe

# A Composição é o tipo de relacionamento de associação "Tem Um" (Has-a) mais forte que existe. Nesse relacionamento, uma classe é construída (ou composta) por instâncias de outras classes, e há uma forte dependência entre elas.

# Características Chave da Composição:
# Dependência Forte (Relação de "Vida Dependente"): O principal diferencial da Composição é que a classe "parte" não tem significado ou existência relevante sem a classe "todo". A classe composta é responsável por criar e, crucialmente, gerenciar o ciclo de vida dos seus componentes.

# Destruição Conjunta: Se o objeto "todo" (o contêiner) é destruído, os objetos "partes" (os componentes) são geralmente destruídos junto com ele. A parte é uma parte integral do todo.




class Select:
    def by_id(self) -> any:
        print("Selecionando um elemento no banco de dados.")


class Insert:
    def insert_value(self) -> None:
        print("Inserindo um valor no banco de dados.")

# classe composta(todo)
class Repositorio:
    def __init__(self) -> None:
        # composicao
        # 1. A Repositorio CRIA e possui as instâncias de Select e Insert
        # Essas instâncias não foram criadas externamente e passadas, mas sim nascem com o Repositorio
        self.__select = Select()
        self.__insert = Insert()

    def select_by_id(self, id: int) -> any:
        self.__select.by_id()


repo = Repositorio()
repo.select_by_id(33)  # output: Selecionando um elemento no banco de dados.
