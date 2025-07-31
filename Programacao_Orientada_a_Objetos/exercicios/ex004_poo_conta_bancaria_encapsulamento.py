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
            self.__saldo += quantia
            return f"Conta bancária de {self.__titular}: depósito de R${quantia:.2f} efetuado com sucesso. Saldo atualizado para R${self.get_consultar_saldo():.2f}"
        else:
            return f"Operação cancelada! Não é possível depositar R${quantia:.2f}. O valor a depositar tem que ser positivo."

    def sacar(self, quantia: float):
        if quantia <= self.__saldo:
            self.__saldo -= quantia
            return f"Conta bancária de {self.__titular}: saque de R${quantia:.2f} efetuado com sucesso. Saldo atualizado para R${self.get_consultar_saldo():.2f}"
        else:
            return f"Operação cancelada! Não é possível sacar quantia de R${quantia:.2f}. Verifique seu saldo para efetuar a operação."

    def get_consultar_saldo(self):
        return self.__saldo


conta_bancaria1 = ContaBancaria("Thaís", 1000)
saldo1 = conta_bancaria1.get_consultar_saldo()
print(f"O saldo da Conta Bancária é  R${saldo1}")
deposito1 = conta_bancaria1.depositar(-10)
print(deposito1)
print(conta_bancaria1.get_consultar_saldo())
deposito2 = conta_bancaria1.depositar(80.9)
print(deposito2)
print(conta_bancaria1.get_consultar_saldo())
saque1 = conta_bancaria1.sacar(2000)
print(saque1)
saldo2 = conta_bancaria1.get_consultar_saldo()
print(f"O saldo da Conta Bancária é  R${saldo2}")
saque2 = conta_bancaria1.sacar(380.90)
print(saque2)
