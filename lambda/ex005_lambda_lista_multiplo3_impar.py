# Exercício 5 (desafiador leve)

# Você tem a lista numeros = list(range(1, 21)).
# Use lambda e filter() para criar uma nova lista com apenas os múltiplos de 3 que também sejam ímpares.

numeros = list(range(1, 21))
impares_multiplos_3 = list(filter(lambda x: x % 3 == 0 and x % 2 == 1, numeros))
print(f"A lista de números é: \n{numeros}")
print(
    f"Os números ímpares divisíveis por 3 na lista de números são: \n{impares_multiplos_3}"
)
