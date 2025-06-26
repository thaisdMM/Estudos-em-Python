# Exercício 1 (fácil)
# Crie uma função lambda que receba um número e retorne o quadrado dele.

dobro = lambda x: x * 2
print(dobro(8))

quadrado = lambda x: x**2

numero = float(input(f"Digite um número para ver o dobro dele "))
print(f"O dobro de {numero} é: {dobro(numero)}")
print(f"O quadrado de {numero} é: {quadrado(numero)}")
