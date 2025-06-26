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

media_alunos = list(map(lambda x: sum(x["notas"]) / len(x["notas"]), alunos))
print(media_alunos)
situacao_aluno = lambda x: (
    "aprovado" if x >= 7 else "recuperação" if x >= 5 else "reprovado"
)
# for i in media_alunos:
#     print(situacao_aluno(i))

# alunos_media_situação = [alunos[:]]
# for i in range(0, len(media_alunos)):
#     # for valor in alunos_media_situação:
#     #     valor["media"] = media_alunos[i]
#         alunos_media_situação[i].append(valor["media"])
#         # print(media_alunos)

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

# alunos_situacao = list(
#     map(
#         lambda x: {"nome": x["nome"], "media": x["media"], "situação":
#             "aprovado"
#             if x["media"] >= 7
#             else "recuperação" if x["media"] >= 5 else "reprovado"
#         },
#         alunos,
#     )
# )

# # x["media"]>= 7 else "recuperação" if x['media']>=5 else "reprovado"}, alunos))

# # alunos_situacao = list(map(lambda x: {"nome": x["nome"], "media": sum(x["notas"])/len(x["notas"]), "situação": "aprovado" if "media">= 7 else "recuperação" if 'media'>=5 else "reprovado"}, alunos))

# print(alunos_situacao)


# alunos_media_situação = []
# for i in range(0, len(media_alunos)):
#     for valor in alunos:
#         print(valor)
#         if valor["notas"]:
#             del valor["notas"]
#         else:
#             continue
#         valor['media'] = media_alunos[i]
#     # print(media_alunos)

# print(alunos)


# alunos_media_situação = []
# for i in range(len(alunos)+1):
#     for valor in alunos:
#         print(valor)
#         valor["media"] = media_alunos[i]
#         print(media_alunos)
# valor['notas'] = valor['media']
# alunos_media_situação.append(alunos[:])
# print(valor)
# print(alunos_media_situação)


# for key, value in alunos.items():
#     for media in media_alunos:
#         alunos_media_situação.append()


# for i in media_alunos:
#     print(situacao_aluno(i))


# for valor in alunos:
#     for notas in valor['notas']:
#         print(notas, end=" ")
#         media_alunos = list(map(lambda x: sum(x) / len(x), notas))
#         print(media_alunos)
#     print()

# for valor in alunos:
#     print(valor['notas'])
#     print(sum(valor['notas']))
#     media = (sum(valor['notas'])/len(valor["notas"]))
#     print(media)
#     media_alunos = list(map(lambda valor["notas"]: (sum(valor['notas'])/len(valor["notas"]), valor["notas"]))
#     print(media_alunos)
#     # media2 = list(map(media, alunos))
#     # print(f"map media {media2}")
# #     notas = list(map(sum(valor["notas"]), alunos))
# # print(notas)
#     # media_alunos = list(map(lambda x: sum(x) / len(x), valor["notas"]))
# print(media_alunos)
# # print()

# print(media_alunos)

# media_alunos = list(map(lambda x: sum(x) / len(x), alunos[3]))
# print(media_alunos)
