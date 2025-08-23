# Classe de conector de banco de dados
class ConectorBancoDeDados:
    def __init__(self) -> None:
        self.connection = None

    def conectar_ao_banco(self) -> None:
        self.connection = True


# Classe que faz ações no banco de dados - inserir dados, busca de dados, update de dados
class RepositorioDeBanco:
    def __init__(self, connexao: ConectorBancoDeDados) -> None:
        self.__conexao = connexao

    def busca_dados(self) -> list:
        if self.__conexao.connection:
            return [1, 2, 3, 4, 5]
        return None


# uma ação que realiza - ex pegar dados do banco
# a RegraDeNegocio está associada ao RepositorioDeBanco que está associada ao ConectorBancoDeDados
class RegraDeNegocio:
    def __init__(self, repo: RepositorioDeBanco) -> None:
        self.__repo = repo

    def calcular_resultados(self) -> None:
        dados = self.__repo.busca_dados()
        if not dados:
            print("Dados não encontrados. Verifique sua conexão com o banco")
        else:
            resposta = 0
            for dado in dados:
                resposta += dado
            print(f"O resultado é: {resposta}")


connetion = ConectorBancoDeDados()
connetion.conectar_ao_banco()

repo = RepositorioDeBanco(connetion)
regra = RegraDeNegocio(repo)

regra.calcular_resultados()
# outupt quando tem conexão: O resultado é: 15
# output quando nao tem conexão: Dados não encontrados. Verifique sua conexão com o banco
