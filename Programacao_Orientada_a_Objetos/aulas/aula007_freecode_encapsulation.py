# # ENCAPSULAMENTO
## Encapsulamento é o princípio de esconder os detalhes internos de implementação de um objeto e expor apenas o que for necessário por meio de uma interface pública controlada (geralmente métodos).

# Para que serve o encapsulamento?

# 1. Proteger os dados
# Impede acesso direto e indevido aos atributos sensíveis de um objeto.
# Evita que o estado interno do objeto seja modificado de forma incorreta.
# 2. Organizar o código
# Deixa o código mais modular e fácil de manter.
# Cada classe controla o seu próprio estado interno.
# 3. Controlar o acesso e comportamento
# Permite criar métodos de acesso controlado como getters (leitura) e setters (modificação), que validam valores antes de alterar um atributo.
# 4. Reduzir acoplamento
# O objeto só expõe o que realmente importa para quem o usa. Assim, quem usa a classe não depende dos detalhes internos dela.

# Withdow encapsulation
# bad example


class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance


account = BadBankAccount(0.0)
account.balance = -1
print(account.balance)  # output: -1

# Encapsulation


class BankAccount:
    def __init__(self):
        self._balance = 0.0

    # get
    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be posive.")
        if amount >= self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount


account = BankAccount()
print(account.balance)
# não colocar o set é bom nesse caso, pois não permite ao usuário modificar o dado,
# ele tem o get para ver, mas não pode modificar
# account.balance = -1 # output: AttributeError: property 'balance' of 'BankAccount' object has no setter
account.deposit(1.99)
print(account.balance)
account.withdraw(1)
print(account.balance)
# account.withdraw(100)  # output: ValueError: Insufficient funds.
