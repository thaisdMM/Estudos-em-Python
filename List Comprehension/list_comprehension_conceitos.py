# # O que é List Comprehension?

# # É uma forma concisa e legível de criar uma nova lista a partir de outra coleção, aplicando:
# # 	•	Transformações,
# # 	•	Filtros,
# # 	•	Ou ambos.

# # Estrutura básica:

# # [expressão for item in coleção if condição]
# # Equivalente ao map() + filter() + for, tudo em uma linha.

# 	1.	Dobrar todos os números de uma lista:

dobrar = [x * 2 for x in [1, 2, 3, 4, 5]]
print(dobrar)


# dividir ítens de uma lista
dividir = [x / 2 for x in dobrar]
print(dividir)

# 2.	Filtrar apenas os pares:

# eu tentando da minha cabeça
pares1 = [x % 2 == 0 for x in [4, 7, 8, 12, 13, 24]]
print(pares1)  # outupt: [True, False, True, True, False, True]

# código do tutorial
pares = [x for x in [4, 7, 8, 12, 13, 24] if x % 2 == 0]
print(pares)  # output: [4, 8, 12, 24]

# 	3.	Criar dicionários com dados processados:
alunos = [
    {"nome": "ana", "notas": [7.5, 8, 10]},
    {"nome": "joão", "notas": [4, 5.5, 6]},
    {"nome": "maria", "notas": [10, 10, 10]},
    {"nome": "carlos", "notas": [6, 6, 5.5]},
    {"nome": "julia", "notas": [8, 7, 6]},
]
alunos_media = [
    {"nome": aluno["nome"], "media": sum(aluno["notas"]) / len(aluno["notas"])}
    for aluno in alunos
]
for alunos in alunos_media:
    print(alunos)

# # # Explicação ampliada: Comparativo com map() e filter()
# map() e filter() podem ser mais legíveis quando o processamento é simples e a função já existe.

# Já list comprehension é mais natural de ler e mais Pythonic, principalmente em código moderno.

# 1- map() :

# Dobrar valores

# MAP() com lambda
lista = [1, 2, 3]
dobrar_lista = list(map(lambda x: x * 2, lista))
print(dobrar_lista)

# LIST COMPREHENSION:
dobrar_lista2 = [x * 2 for x in lista]
print(dobrar_lista2)

# 2- FILTER()

# filter() com lambda:
lista = [1, 2, 3, 4]
pares = list(filter(lambda x: x % 2 == 0, lista))
print(pares)

# LIST COMPREHENSION:
pares2 = [x for x in lista if x % 2 == 0]
print(pares2)

# Conclusão e próximos passos

# Ainda não exploramos:
# 	•	aninhamento de list comprehensions;
# 	•	uso com estrutura de dicionários mais complexas;
# 	•	criação de condições múltiplas.

# Mas para o momento, está mais do que suficiente.
