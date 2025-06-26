#  Exercício 3 (médio)
# Crie uma função lambda que receba dois números (x, y) e retorne a soma dos quadrados de ambos.
# Dica: você pode usar lambda x, y: ...

soma_quadrado_numeros = lambda x, y: (x * 2) + (y * 2)
numero1 = int(input("Número 1 = "))
numero2 = int(input("Numero 2= "))
print(soma_quadrado_numeros(numero1, numero2))
