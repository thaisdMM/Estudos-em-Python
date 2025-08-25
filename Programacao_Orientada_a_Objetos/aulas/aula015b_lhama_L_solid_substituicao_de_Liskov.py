# PRINCÍPIO DE LISKOV - L de SOLID


class ConnectionDB:
    def conectar(self):
        print("Conectando ao banco de dados")


class SqlRepository(ConnectionDB):
    def select(self):
        print("Buscando dados no banco SQL")


class NoSQLRepository(ConnectionDB):
    def selec(self):
        print("Buscando dados no banco NoSQL")


# Caso 1: quebra do princípio de Liskov
#  Quebra da hierarquia:
#  Fazer DBHandler herdar de NoSQLRepository está incorreto, pois um DBHandler não é um tipo de NoSQLRepository.
#  A principal quebra do Liskov ocorre quando o método select() é sobrescrito para levantar uma exceção.


class DBHandler(NoSQLRepository):
    def alterTable(self):
        print("Alterando tabela em SQL")

    # Caso 1: quebra do princípio de Liskov -> o método select aqui é sobrescrito
    def select(self):
        raise Exception("Não busca dados no banco NoSQL")


# Caso 2: sem quebra do Princípio de Liskov
# Hierarquia de Herança Correta: A classe DBHandler2 herda de SqlRepository.
#  Esta é uma relação "é-um": uma funcionalidade de alterTable específica para bancos de dados SQL.
# Ao herdar de SqlRepository, o DBHandler2 ganha todas as suas funcionalidades, como o método select(), e a substituição funcionaria corretamente se o DBHandler2 fosse usado no lugar de um SqlRepository.


class DBHandler2(SqlRepository):
    def alterTable(self):
        print("Alterando tabela em SQL")


handler = DBHandler2()
handler.conectar()  # output: Conectando ao banco de dados

# Comportamento Consistente: O método select() não é sobrescrito para causar um erro ou comportamento inesperado.
# Ele é herdado diretamente de SqlRepository e funciona como esperado.
# Assim, qualquer código que espere um SqlRepository pode receber um DBHandler2 sem causar problemas.

handler.select()  # output: Buscando dados no banco SQL
handler.alterTable()  # output: Alterando tabela em SQL
