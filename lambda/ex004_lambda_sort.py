# Exercício 4 (médio)

# Dada a lista nomes = ['ana', 'joão', 'maria', 'pedro'], use lambda e sorted() para ordenar os nomes pela última letra de cada nome.

nomes = ["ana", "joão", "caroline", "maria", "mateus", "pedro"]
ordenada = sorted(nomes, key=lambda x: x[-1])
print(f"lista normal: \n{nomes}")
print(f"Lista ordenada de acordo com a última letra: \n{ordenada}")
