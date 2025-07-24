## 1- Static Attributes(class attribute)
# Atributo de classe (estático): pertence à classe e é compartilhado por todas as instâncias.
# atributo de classe é diferente de atributo de instancia
# > # Atributo de instância: pertence a cada objeto; cada instância tem seu próprio valor.


## is an attribute that belongs to the class itself, not to any specific instance of the class.
## útil para configuração ou para funções que serão compartilhadas por todos, etc...


class User:
    # static attribute:
    # > criado uma vez
    user_count = 0

    def __init__(self, username, email):
        # instance attribute
        # Pertence somente ao objeto específico criado da classe.
        # Cada objeto tem sua cópia independente desse atributo.
        self.username = username
        self.email = email
        # o atributo estático pertence a classe, não é criado em cada objeto, mas
        # > como chamamos ele aqui, ele vai ser incrementado cada vez que criar um novo objeto(User)
        User.user_count += 1

    ## Método de instância: usa 'self' e pode acessar/alterar os dados do objeto.
    def display_user(self):
        print(f"Username: {self.username}, Email: {self.email}")


user1 = User("Senku", "drstone@stoneage.com")
user2 = User("Taiju", "bigoaf@stoneage.com")

print(User.user_count)  # output: 2
# dá para acessar assim:
print(user1.user_count)  # output: 2
print(user2.user_count)  # output: 2
user2.display_user()

# 2- Static Methods

# is a method that belongs to the class itself rather than any instance of the class.
# to define a static method we use `@staticmethod`` decorator

# Static Methods vs. Instance Method Example


class BankAccount:
    # static attribute:
    MIN_BALANCE = 100

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    # instance => existe em cada objeto que for criado
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.owner}'s new balance: ${self._balance}")
        else:
            print("Deposit amount must be positive.")

    ## Static method
    ## É uma função dentro da classe que não depende do estado de nenhum objeto (self) nem da própria classe (cls).
    ##  é apenas uma função utilitária agrupada dentro da classe.

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5


account = BankAccount("Alice", 500)
account.deposit(200)  # output: Alice's new balance: $700

## Static method - existe na classe, para acessar:
print(BankAccount.is_valid_interest_rate(3))  # output: True
print(BankAccount.is_valid_interest_rate(10))  # output: False

## 3- Protected and private methods


class BankAccount:
    # static attribute:
    MIN_BALANCE = 100

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    # instance => existe em cada objeto que for criado
    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            self.__log_transation("deposit", amount)
        else:
            print("Deposit amount must be positive.")

    ## protected method
    def _is_valid_amount(self, amount):
        return amount > 0

    ## private method
    ## Não pode acessar fora da classe
    def __log_transation(self, transation_type, amount):
        print(f"Logging {transation_type} of ${amount}. New balance: ${self._balance}")

    ## Static method
    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5


account = BankAccount("Alice", 500)
account.deposit(200)  # output: Logging deposit of $200. New balance: $700

## Static method - existe na classe, para acessar:
print(BankAccount.is_valid_interest_rate(3))  # output: True
print(BankAccount.is_valid_interest_rate(10))  # output: False

# ERRO: método privado, não pode ser acessado fora da classe
# account.__log_transation(
#     "withdraw", 300
# )  ## output: AttributeError: 'BankAccount' object has no attribute '__log_transation'
