# 1- acessing object data


class User:
    def __init__(self, username, email, passoword):
        self.username = username
        self.email = email
        self.passoword = passoword

    def say_hi_to_user(self, user):
        print(
            f"Sending massage to {user.username}: Hi {user.username},it's {self.username}"
        )


user1 = User("robynwood", "robyn@gmail.com", "123")
user2 = User("batman", "bat@outlook.com", "abc")

user1.say_hi_to_user(user2)
# output: Sending massage to batman: Hi batman,it's robynwood

# modifying object data


class User:
    def __init__(self, username, email, passoword):
        self.username = username
        self.email = email
        self.passoword = passoword

    def say_hi_to_user(self, user):
        print(
            f"Sending massage to {user.username}: Hi {user.username},it's {self.username}"
        )


user1 = User("robynwood", "robyn@gmail.com", "123")

print(user1.email)  # output: robyn@gmail.com
user1.email = "rob@gmail.com"
print(user1.email)  # output: rob@gmail.com
# dá para mofificar para qualquer informção que quiser e isso não é bom. ex:
user1.email = "jin"
print(user1.email)  # output: jin

# 2- Acessing and Modifying Data:
# 1- The traditional way: make the data private and use getters and setters:


class User:
    def __init__(self, username, email, passoword):
        self.username = username
        # atributo protegido _ desses antes do nome ex: _email
        self._email = email
        self.passoword = passoword


def get_email(self):
    return self._email


user1 = User("robynwood", "robyn@gmail.com", "123")
# não pode acessar um atributo protegido fora da classe:
# em python você consegue acessar o método protegido, fora da classe, mas é errado ainda assim.
# > o código abaixo está errado:
# print(user1._email)


class User:
    def __init__(self, username, email, passoword):
        self.username = username
        # atributo protegido _ desses antes do nome ex: _email
        self._email = email
        self.passoword = passoword

    # utilizando um método para usar o atributo protegido
    def clean_email(self):
        return self._email.lower().strip()


user1 = User("robynwood", "  Robyn@gmail.com  ", "123")

print(user1.clean_email())

# PRIVATE != PROTECTED
# Name Mangled(Python "troca o nome do atributo")


class User:
    def __init__(self, username, email, passoword):
        self.username = username
        # atributo PRIVADO __ 2 desses antes do nome ex: __email
        self.__email = email
        self.passoword = passoword

    # utilizando um método para usar o atributo protegido
    def clean_email(self):
        return self.__email.lower().strip()


user1 = User("robynwood", "  Robyn@gmail.com  ", "123")

# #impossível acessar fora da classe quando é privado - Python "troca o nome do atributo"
# print(user1.__email)
# output an ERROR: AttributeError: 'User' object has no attribute '__email'

print(user1.clean_email())

# ## when to use protected vs private attributes?
# # normalmente usa o protegido.
# # usa o privado quando é extremamente necessário.

## Creating getter and setter methods

## Why do we create getters and setters?
from datetime import datetime


class User:
    def __init__(self, username, email, passoword):
        self.username = username
        # atributo PROTEGIDO
        self._email = email
        self.passoword = passoword

    # esse jeito é convencional
    def get_email(self):
        ## Why do we create getters and setters?
        ## pode controlar se a pessoa tem autorização para acessar esse email
        ## controla a hora que o email foi acessado
        print(f"Email acessed at {datetime.now()}")
        return self._email

    # def set_email(self, new_email):
    #     self._email = new_email
    # colocando um pouco de validação lógica no set método:
    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email


user1 = User("robynwood", "robyn@gmail.com", "123")

print(user1.get_email())
user1.set_email("rob@outlook.com")
print(user1.get_email())

# para evitar esse tipo de dado vamos adicionar uma pequena lógica no set método
user1.set_email("2345gfg")
print(user1.get_email())  # output: 2345gfg
# rodando o print depois da validação com o if:
# caso 1 o email não foi atualizado outup: Email acessed at 2025-07-04 19:01:17.153200 rob@outlook.com

user1.set_email("2345@gfg.com")
print(user1.get_email())
# aqui é atualizado: Email acessed at 2025-07-04 19:06:08.418298 2345@gfg.com

# Acessing e Modifying Data:
# 2- Properties - get and set properties -> Python way


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


user1 = User("danthman", "dan@gmail.com", "123")
# acessando o atritubuto diretamente e passando um dando inválido:
user1.email = "This is not an email"
print(user1.email)  # output: This is not an email

# jeito de corrigir o exemplo acima:


class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    # getter poperty
    @property
    def email(self):
        print("Email acessed")
        return self._email

    # setter property
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self.email = new_email


user1 = User("danthman", "dan@gmail.com", "123")
## acessando o atritubuto diretamente e passando um dando inválido:
## antes de ter o setter property não dá para modificar o dado, só acessar, o codigo abaixo dá ERRO
# user1.email = "This is not an email"
# print(user1.email)
# #output: user1.email = "This is not an email" AttributeError: property 'email' of 'User' object has no setter

# parece que está acessando diretamente, mas esta acessando a propriedade
# esse jeito é bom, pois se antes não era privado e depois passou a ser, não muda o código, pois o meio de acesso é o mesmo, basta adicionar os código da @property
print(user1.email)  # output Email acessed dan@gmail.com

## depois de ter o setter property

user1.email = "This is not an email"
print(user1.email)
## output: não aceita o novo email, por causa da valição
# Email acessed dan@gmail.com
