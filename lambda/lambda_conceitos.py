# Uma função lambda é uma função anônima (ou seja, sem nome), usada quando queremos criar uma função pequena e simples, geralmente para uso imediato ou como argumento de outra função.

#  Quando usar lambda?

# Use lambda quando:
# 	•	A função for simples
# 	•	Você for passar essa função como argumento para outra
# 	•	Você não precisa reutilizar a função em vários lugares do código

# Evite lambda se:
# 	•	A lógica for complexa
# 	•	For preciso tratamento de erro
# 	•	Você precisar de clareza para manutenção futura

# estrutura básica:
# lambda argumentos: expressão
# > não usa def nem return
# > tudo deve estar em uma única linha
# > a expressão é o valor retornado automaticamente

# diferença entre lambda e def


def dobrar(x):
    return x * 2


dobrar2 = lambda x: x * 2


# Você chama a função lambda do mesmo jeito que chama uma função normal: com parênteses e o valor dentro.

print(dobrar(6))
print(dobrar2(6))
x = 12
print(dobrar(x))
print(dobrar2(x))

# 1. Lambda atribuído a uma variável (uso comum e reutilizável)
# Boa legibilidade
# •	Fácil de reutilizar
# •	Útil quando você precisa aplicar a mesma lógica várias vezes

dobrar2 = lambda x: x * 2
print(dobrar2(5))


# # 2. Lambda usado diretamente (sem nome / sem variável) - função lambda imediata ou função anônima autoexecutável
# Geralmente, usado quando:
# 	•	A função é pequena
# 	•	Você só vai usar ela uma vez
# 	•	E não precisa de clareza do nome

print((lambda x: x * 2)(5))


# lambda como argumento
valores = [3, 1, 4, 2]
ordenado = sorted(valores)
print(valores)
print(ordenado)  # output: [1, 2, 3, 4]
ordenado_lambda = sorted(valores, key=lambda x: -x)  # -x ordenou de trás pra frente
print(ordenado_lambda)  # output: [4, 3, 2, 1]

# Ordenando uma lista de tuplas pelo segundo item[1]

pares = [(1, 5), (2, 3), (4, 1)]
pares_ordenados = sorted(pares, key=lambda x: x[1])
print(pares)
print(pares_ordenados)  # Saída: [(4, 1), (2, 3), (1, 5)]

# Ordenando pelo primeiro item[0]
pares2 = [(7, 5), (5, 3), (2, 1)]
pares2_ordenados0 = sorted(pares2, key=lambda x: x[0])
print(pares2)
print(pares2_ordenados0)  # output : [(2, 1), (5, 3), (7, 5)]

# MAP

# map() é uma função embutida (built-in) do Python que serve para aplicar uma função a cada item de uma sequência (como uma lista).
# Ou seja, ela mapeia (transforma) os elementos de uma coleção, um por um, de acordo com a função que você fornecer.

# Estrutura map()
# map(funcao, iteravel)
# # funcao: é a função que será aplicada a cada item
# # iteravel: é uma coleção como list, tuple, etc
# O map() retorna um iterador (não uma lista diretamente), por isso normalmente usamos list() para ver o resultado.


# map com def
def dobrar(x):
    return x * 2


numeros = [1, 2, 3, 4]
dobrados_def = list(map(dobrar, numeros))
print(numeros)
print(dobrados_def)

# # LAMBDA - Aplicando uma função a cada item de uma lista com map

numeros = [1, 2, 3, 4]
dobrados_lambda = list(map(lambda x: x * 2, numeros))
print(numeros)
print(dobrados_lambda)

## FILTER

# filter() função embutida do Python que filtra os elementos de uma coleção, mantendo apenas os que retornarem True em uma condição.
# Ou seja, aplica uma função booleana (que retorna True ou False) e filtra os valores de acordo com essa condição.

# Estrutura filter()
# # filter(funcao, iteravel)
# funcao: uma função que retorna True ou False
# iteravel: uma lista ou outro tipo de sequência
# O resultado também é um iterador → usamos list() para ver o resultado.

# FILTER com DEF


def par(x):
    return x % 2 == 0


valores = [10, 15, 22, 33, 40]
pares_def = list(filter(par, valores))
print(valores)
print(pares_def)  # Saída: [10, 22, 40]

# FILTER com LAMBDA

valores = [10, 15, 22, 33, 40]
pares_lambda = list(filter(lambda x: x % 2 == 0, valores))
print(valores)
print(pares_lambda)  # Saída: [10, 22, 40]
# lambda x: x % 2 == 0 → retorna True para números pares
# filter() aplica isso a cada número
# Resultado: apenas os valores pares são mantidos

# # 1. lambda só pode conter uma expressão

# # Mas não pode ter:
# # Várias instruções (print, append, etc.)
# # if com else separados em blocos
# # ex

# ERRO
# lambda x:
#     if x > 0:
#         return x * 2   # ❌ ERRO — isso exige blocos e `return`, proibidos em `lambda`


# CORRETO
# Você até pode usar if em forma de expressão condicional, por exemplo:

lambda x: x * 2 if x > 0 else 0
dobro = lambda x: x * 2 if x > 0 else 0
print(dobro(-1))  # output: 0
print(dobro(5))  # output: 10

# 2. Evite lambda para lógicas complexas
# se ver que é complexo use def

# 3. Você pode usar lambda em estruturas como listas e dicionários

funcoes = {"dobro": lambda x: x * 2, "triplo": lambda x: x * 3}
print(funcoes["dobro"](6), funcoes["triplo"](8))
