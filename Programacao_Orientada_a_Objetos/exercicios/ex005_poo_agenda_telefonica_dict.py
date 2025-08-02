# Exercício 3 – Agenda Telefônica (com dicionário interno)
# Descrição:
# Crie uma classe Agenda que armazena contatos com nome e telefone. Você deve permitir adicionar, remover, buscar contatos, e mostrar todos os contatos salvos.

# Objetivos:

# Trabalhar com atributos protegidos ou privados
# Usar estruturas de dados dentro da classe (dict)
# Pensar em como estruturar ações (métodos) comuns em um sistema real
# Dica de raciocínio:
# Você pode guardar os contatos como chave-valor (nome: telefone), mas pense também no que fazer quando alguém tenta adicionar um nome já existente, ou buscar um nome que não está cadastrado. O raciocínio aqui é mais importante que o código em si.


class Agenda:
    def __init__(self):
        self._lista_contatos = []

    def adicionar_contato(self):
        while True:
            nome = input("Nome do contato: ").strip().title()

            nome_existe = self.validar_dados(nome)
            if nome_existe:
                print(
                    f"{nome} já existe na lista de contatos, por favor adicione outro nome."
                )
                continue
            else:

                numero_telefone = input("Número de telefone: ").strip()
                contato = {"nome": nome, "telefone": numero_telefone}
                self._lista_contatos.append(contato.copy())
            continuar = input("Quer continuar? S/N ").strip().upper()[0]
            if continuar not in "NS":
                print("Resposta inválida. Responda S para continuar ou N para parar.")
            if continuar == "N":
                break
            # return self._lista_contatos

    @property
    def contatos(self):
        return self._lista_contatos

    def exibir_contatos(self):
        print("Lista de contatos: ")
        print()
        for contato in self.contatos:
            for key, value in contato.items():
                print(f"{key}: {value} | ", end="")
            print()
        print()

    def excluir_contatos(self):
        print("Excluir contato:\n")
        nome = input("Nome do contato: ").strip().title()
        contato_existe = self.buscar_contato(nome)
        if contato_existe:
            self._lista_contatos.remove(contato_existe)
            return "Contato excluido com sucesso!"
        else:
            return "Nome do contato não existe na agenda."

    def validar_dados(self, nome):
        if any(
            nome_existente["nome"] == nome for nome_existente in self._lista_contatos
        ):
            return True
        return False

    def buscar_contato(self, nome):
        for contato in self._lista_contatos:
            if contato["nome"] == nome:
                return contato
        return None


# função
def continuar():
    while True:
        continuar = input("Quer continuar? S/N ").strip().upper()[0]
        if continuar not in "NS":
            print("Resposta inválida. Responda S para continuar ou N para parar.")
        if continuar == "N":
            break


agenda1 = Agenda()
contato1 = agenda1.adicionar_contato()
# print(contato1)
ver_contatos = agenda1.exibir_contatos()
apagar_contato = agenda1.excluir_contatos()
print(apagar_contato)
ver_contatos2 = agenda1.exibir_contatos()
