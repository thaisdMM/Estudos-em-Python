# DESAFIO: Lista de alunos e aproveitamento escolar

# Você tem uma lista de dicionários, onde cada dicionário representa um aluno com nome e uma lista de notas:
# 1.	Crie uma nova lista onde cada aluno terá:
# 	•	O nome original
# 	•	A média das notas (calculada com map() ou list comprehension + lambda)
# 	•	A situação, de acordo com a média:
# 	•	“aprovado” se média ≥ 7
# 	•	“recuperação” se média ≥ 5 e < 7
# 	•	“reprovado” se média < 5
# 	2.	Ordene essa nova lista pela média (ordem decrescente) usando sorted() com lambda.
# 	3.	Imprima o resultado final, com todos os campos organizados.

# Requisitos técnicos:
# 	•	Você deve usar lambda obrigatoriamente, combinando com:
# 	•	map() ou list comprehension
# 	•	sorted()
# 	•	Expressões condicionais dentro do lambda (ex: condição_if if ... else ...)
# 	•	Não pode usar def para as funções principais (exceto se for testar por fora)
# 	•	O código precisa ser legível e funcional


alunos = [
    {"nome": "ana", "notas": [7.5, 8, 10]},
    {"nome": "joão", "notas": [4, 5.5, 6]},
    {"nome": "maria", "notas": [10, 10, 10]},
    {"nome": "carlos", "notas": [6, 6, 5.5]},
    {"nome": "julia", "notas": [8, 7, 6]},
]

# media_alunos = list(map(lambda x: sum(x["notas"]) / len(x["notas"]), alunos))
# print(media_alunos)
# situacao_aluno = lambda x: (
#     "aprovado" if x >= 7 else "recuperação" if x >= 5 else "reprovado"
# )
# for i in media_alunos:
#     print(situacao_aluno(i))

print(alunos)
alunos_situacao = list(
    map(
        lambda x: {
            "nome": x["nome"],
            "media": sum(x["notas"]) / len(x["notas"]),
            "situação": (
                "aprovado"
                if sum(x["notas"]) / len(x["notas"]) >= 7
                else (
                    "recuperação"
                    if sum(x["notas"]) / len(x["notas"]) >= 5
                    else "reprovado"
                )
            ),
        },
        alunos,
    )
)
print("Lista sem ordenação:")
for aluno in alunos_situacao:
    print(aluno)

print("\n Lista com ordenação por média descrecente:")
ordem_alunos_media = sorted(alunos_situacao, key=lambda x: x["media"], reverse=True)
for aluno in ordem_alunos_media:
    print(aluno)
