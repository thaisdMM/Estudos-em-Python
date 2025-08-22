## SOLID
## S -  Single Responsabilitty/Responsabilidade Única
## um "módulo"/"classe" deve ter responsabilidade sobre uma única parte da funcionalidade fornecida pelo software


class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        # está validando os dados se realmente são str e int
        if isinstance(nome, str) and isinstance(
            idade, int
        ):  # 1- validar é uma responsabilidade
            print(
                "Acessando o banco de dados..."
            )  # 2- acessar banco de dados é outra reponsabilidade
            print(f"Cadastrar usuário {nome}, idade {idade}")
        else:
            print("dados inválidos")  # 3- tratamento de erros outra responsabilidade


sistema1 = SistemaCadastral()
sistema1.cadastrar("Miguel", 15)

## como resolver com o princípio da responsabilidade única:


## usar métodos privados
class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__validate_input(nome, idade):
            self.__resgister_user(nome, idade)
        else:
            self.__error_handle()

    # separou as responsabilidades em módulos, mas poderia ser em classes.
    # se mexer somente nesse codigo, não atrapalha o projeto

    # 1- validação
    def __validate_input(self, nome: str, idade: int) -> bool:
        # está validando os dados se realmente são str e int
        return isinstance(nome, str) and isinstance(idade, int)

    # 2- acessar banco de dados
    def __resgister_user(self, nome: str, idade: int) -> None:
        print("Acessando o banco de dados...")
        print(f"Cadastrar usuário {nome}, idade {idade}")

    # 3- tratamento de erros outra responsabilidade
    def __error_handle(self) -> None:
        print("dados inválidos")


sistema = SistemaCadastral()
sistema.cadastrar("Thaís", 30)
# output: Acessando o banco de dados...
# Cadastrar usuário Thaís, idade 30
sistema.cadastrar("Pedro", "17a")  # output: dados inválidos
