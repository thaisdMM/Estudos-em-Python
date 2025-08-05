# # 6. Contexto de classe vs contexto de objeto
# Classe:
# Tudo que é compartilhado entre todos os objetos
# Armazena atributos estáticos
# Não depende de instâncias
#  Serve, por exemplo, para:
# Definir constantes compartilhadas
# Controlar contadores de instâncias
# Aplicar configurações comuns
# Compartilhar estado global entre objetos


# Objeto:
# Cada instância tem seu próprio contexto
# Armazena dados individuais
# Pode criar atributos próprios mesmo que eles tenham o mesmo nome dos da classe


class MinhaClasse:
    def __init__(self, estado) -> None:
        # contexto de classe, nesse caso o atributo privado, só é acessado dentro da classe
        self.__estado = estado
        print(self.__estado)


# contexto do objeto
objeto = MinhaClasse(True)
##print(objeto.__estado) # vai dar erro

## ATRIBUTO ESTÁTICO DA CLASSE


class MinhaClasse:

    # atributo estático é um atributo de classe: isso significa que não está vinculado a nenhum objeto individualmente, mas sim à classe como um todo. -> o valor dele é unico tanto pra classe, quanto para objetos
    estatico = "lhama"

    def __init__(self, estado) -> None:
        # contexto de classe, nesse caso o atributo privado, só é acessado dentro da classe
        self.__estado = estado


# contexto do objeto
objeto1 = MinhaClasse(True)
objeto2 = MinhaClasse(True)

# Tanto objeto1.estatico quanto objeto2.estatico acessam esse atributo através da classe, mesmo que pareça que estão acessando pelo objeto.
print(objeto1.estatico)  # output: lhama
print(objeto2.estatico)  # output: lhama
## o contexto da classe consegue ser acessado, sem necessariamente criar um objeto para isso
print(MinhaClasse.estatico)  # output: lhama

# se trocar o valor, muda pra todos, inclusive para os objetos que já foram construídos antes da alteração
## -> altera o contexto da clase e altera do objeto, pois todos os objetos ainda estão "olhando" para a classe

MinhaClasse.estatico = "programador"

print(objeto1.estatico)  # output: programador
print(objeto2.estatico)  # output: programador
print(MinhaClasse.estatico)  # output: programador

MinhaClasse.estatico = "programador"
# espelha a idéia de estático e altera somente para esse objeto1
# sso se chama shadowing (sombreamento): o novo atributo “sombra” o atributo da classe, ou seja, o objeto1.estatico agora acessa um valor próprio, local do objeto, que esconde o valor da classe.
objeto1.estatico = "olaMundo"

print(objeto1.estatico)  # output: olaMundo
print(objeto2.estatico)  # output: programador
print(MinhaClasse.estatico)  # output: programador

MinhaClasse.estatico = "programador"
# espelha a idéia de estático e altera somente para esse objeto1
objeto1.estatico = "olaMundo"
MinhaClasse.estatico = "LhamaAqui"

print(objeto1.estatico)  # output: olaMundo
print(objeto2.estatico)  # output: LhamaAqui
print(MinhaClasse.estatico)  # output: LhamaAqui
