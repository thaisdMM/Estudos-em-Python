# Princípio da INJEÇÃO DE DEPEDÊNCIA

# uma classe está diretamente associada a outra
# A Injeção de Dependência é um princípio de design de software que busca diminuir o acoplamento entre as classes.
# Em vez de uma classe criar a sua própria dependência, ela recebe essa dependência de "fora"(injetada).

# o livro do Clean Code, dependencia deve ser tratado como elemento privado no codigo:
##-> uma vez que a dependência é injetada, ela se torna um detalhe interno da classe e não deve ser acessada ou manipulada diretamente de fora
## Isso está alinhado com o Princípio do Encapsulamento, que sugere que os detalhes de implementação de uma classe devem ser ocultados.
## apesar do professor usar __ em alguns estudos essa prática não é recomendada por causa do name mangling:
## ->  Em Python, a forma mais idiomática e recomendada de implementar esse princípio é com o uso do único underscore (_). Ele sinaliza a intenção de encapsulamento sem a complexidade desnecessária do name mangling.


class Celular:
    def __init__(self, modelo: str) -> None:
        self.modelo = modelo

    def enviar_mensagem(self, mensagem: str) -> None:
        print(f"Enviando mensagem: {mensagem}")

    def abrir_emails(self) -> None:
        print("Abrindo os emails.")

    def abrir_youtube(self) -> None:
        print("Abrindo Youtube...")


# injeção de dependencia: a classe pessoa depende de celular -> atributo da classe
class Pessoa:
    def __init__(self, celular: Celular) -> None:
        self.__celular = celular

    def pedir_pizza(self) -> None:
        print("Buscando o celular...")
        print("Definindo o sabor...")
        # chama pelo atributo
        self.__celular.enviar_mensagem("Quero uma pizza de calabresa.")
        print("Aguardando a chegada.")

    def estudar(self) -> None:
        print("Sentando na sala de estudos...")
        self.__celular.abrir_youtube()
        print("Anotando o conteúdo.")


android = Celular("Samsung")
iphone = Celular("Iphone")

# Erro abaixo:  para criar um objeto tem que colocar o celular
# pessoa = Pessoa() # output: TypeError: __init__() missing 1 required positional argument: 'celular'

reginaldo = Pessoa(android)
marlene = Pessoa(iphone)

reginaldo.pedir_pizza()
print()
marlene.estudar()
