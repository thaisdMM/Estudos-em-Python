# Exercício 2 (fácil)
# Use lambda e map() para transformar a lista [2, 4, 6, 8] em uma nova lista com os valores divididos por 2.

# 1
numeros = [2, 4, 6, 8]
metade = list(map(lambda x: x / 2, numeros))
print(numeros)
print(metade)

# 2 criando lista com input e fazendo lambda metada

lista_numeros = []
for i in range(0, 5):
    lista_numeros.append(int(input("Digite 5 números inteiros para compor uma lista ")))
print(lista_numeros)
metade = list(map(lambda x: x / 2, lista_numeros))
print(f"A medade dos número da lista {lista_numeros} é: {metade}")
