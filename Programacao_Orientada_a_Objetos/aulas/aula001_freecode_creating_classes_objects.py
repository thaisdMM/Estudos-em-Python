# name = "Thais" # name = recebe uma string como objeto "Thais"
# age = 29

# print(type(name)) # outpt: <class 'str'> ## name é objeto da classe str
# print(type(age)) # <class 'int'> ## age é um int objeto, age é obejeto da classe int

# # objetos diferentes tem comportamentos diferentes, string tem comportamento diferente de interger

# # a classe string tem o objeto string  métodos, funcções diferente que operam e manipulam o dado da string
# ## a classe define como o objeto será
## "o método é pratica a funçao da classe"
# print(name.upper())

## 1- Creating Classes and objects

# criando uma classe Dog:

# no codigo abaixo os objetos eram iguais só usavam o método bark, abaixo teremos atributos que faram os objetos dog1 e dog2 serem diferente

# class Dog:
#     # metodo chamado bark
#     def bark(self):
#         print("Whoof whoof")

# # criando objetos da classe Dog e passando uma variável chamada dog

# dog1 = Dog()
# # Acessando o método do dog1 object
# dog1.bark()

# dog2 = Dog()
# dog2.bark()


# agora com o atributo(data field) dá para diferenciar um objeto do outro
class Dog:
    # __init__ método ## para fazer data field (ATRIBUTO) dá para acessar com o .  o . também acessa os métodos
    # o nome não precisa ser o mesmo, mas é convenção colocar o mesmo
    # o __init__ método apenas roda uma vez quando o objeto é istanciado
    ## > ex de objto instânciado: Dog("Bruce", "Scottish Terrier")
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # metodo chamado bark
    def bark(self):
        print("Whoof whoof")


# criando objetos da classe Dog e passando uma variável chamada dog
# dog1 é a variável que recebe o objeto Dog()

# o que está assinado é unico para cada variável dog1 e dog2
dog1 = Dog("Bruce", "Scottish Terrier")
# Acessando o método do dog1 object
dog1.bark()
print(dog1.name)
print(dog1.breed)

dog2 = Dog("Freya", "Greyhound")
dog2.bark()
print(dog2.name)
print(dog2.breed)

## 2- Combining objects
