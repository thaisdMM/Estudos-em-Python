# Exercício 2 – Conta Bancária (com encapsulamento)
# Descrição:
# Crie uma classe ContaBancaria com atributos privados: __titular, __saldo. A classe deve ter métodos para depositar, sacar e consultar saldo.

# Objetivos:

# Usar atributos privados
# Praticar encapsulamento com métodos de acesso (get/set ou @property)
# Raciocinar sobre limites (por exemplo, impedir saque de valor maior que o saldo)
# Restrição:
# Você deve proteger os dados contra manipulação direta.

# Dica de raciocínio:
# Pense que o cliente do banco não pode simplesmente “editar” o saldo. Ele precisa seguir regras, como “não pode sacar mais do que tem”. A lógica dos métodos precisa proteger os dados da classe contra uso indevido.


class ContaBancaria:
    def __init__(self, titular: str, saldo: float):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, quantia: float):
        if quantia > 0:
            deposito = quantia
            self.__saldo += quantia
            return deposito
        else:
            return False

    def sacar(self, quantia: float) -> bool:
        if quantia <= self.__saldo:
            self.__saldo -= quantia
            return True
        else:
            return False

    def get_consultar_saldo(self):
        return self.__saldo

    def deposito_mensagem(self, quantia):
        deposito = self.depositar(quantia)
        if deposito:
            mensagem = f"Conta bancária de {self.__titular}: depósito de R${deposito} efetuado com sucesso. Saldo atualizado para {self.get_consultar_saldo()}"
        else:
            mensagem = "Operação cancelada! Não é possível depositar quantia R$0,00 ou negativa"
        return mensagem

    def sacar_mensagem(self, quantia: float):
        if self.sacar(quantia) == True:
            mensagem = f"Conta bancária de {self.__titular}: saque de R${quantia} efetuado com sucesso. Saldo atualizado para {self.get_consultar_saldo()}"
        else:
            mensagem = "Operação cancelada! Não é possível sacar quantia maior do que o saldo bancário"
        return mensagem


# class SituacaoContaBancaria(ContaBancaria):
#     def __init__(self, titular: str, saldo: float):
#         super().__init__(titular, saldo)

#     def deposito_mensagem(self, quantia: float):
#         if self.depositar(quantia) == True:
#             mensagem = f"Conta bancária de {self.__titular}: depósito de R${quantia} efetuado com sucesso. Saldo atualizado para {self.get_consultar_saldo}"
#         else:
#             mensagem = "Operação cancelada! Não é possível depositar quantia R$0,00 ou negativa"
#         return mensagem

#     def sacar_mensagem(self, quantia: float):
#         if self.sacar(quantia) == True:
#             mensagem = f"Conta bancária de {self.__titular}: saque de R${quantia} efetuado com sucesso. Saldo atualizado para {self.get_consultar_saldo}"
#         else:
#             mensagem = "Operação cancelada! Não é possível sacar quantia maior do que o saldo bancário"
#         return mensagem


conta_bancaria1 = ContaBancaria("Thaís", 1000)
saldo1 = conta_bancaria1.get_consultar_saldo()
print(f"O saldo da Conta Bancária é  R${saldo1}")
conta_bancaria1.depositar(-10)
mesagem_deposito1 = conta_bancaria1.deposito_mensagem(-10)
print(mesagem_deposito1)
print(conta_bancaria1.get_consultar_saldo())
conta_bancaria1.depositar(80.9)
saldo2 = conta_bancaria1.get_consultar_saldo()
print(saldo2)
mesagem_deposito2 = conta_bancaria1.deposito_mensagem(80.9)
print(mesagem_deposito2)

print(conta_bancaria1.get_consultar_saldo())
conta_bancaria1.sacar(2000)
saldo3 = conta_bancaria1.get_consultar_saldo()
print(saldo3)
mesagem_saque1 = conta_bancaria1.sacar_mensagem(2000)
print(mesagem_saque1)

# tentando separar as responsabilidades, mas nesse caso as messagens ao receber as operação:

# O saldo da Conta Bancária é  R$1000
# Operação cancelada! Não é possível depositar quantia R$0,00 ou negativa
# 1000
# 1080.9
# Conta bancária de Thaís: depósito de R$80.9 efetuado com sucesso. Saldo atualizado para 1161.8000000000002
# 1161.8000000000002
# 1161.8000000000002
# Operação cancelada! Não é possível sacar quantia maior do que o saldo bancário
