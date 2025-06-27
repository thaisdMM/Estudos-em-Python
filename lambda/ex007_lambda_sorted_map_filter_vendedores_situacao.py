# Com base nessa lista:
# 	1.	Calcule a média de vendas de cada vendedor (usando map e lambda)
# 	2.	Classifique a situação de cada um:
# 	•	“excelente” se a média for >= 1000
# 	•	“bom” se a média for >= 700 e < 1000
# 	•	“baixo” se for < 700
# 	3.	Gere uma nova lista de dicionários contendo:
# 	•	"nome"
# 	•	"media_vendas"
# 	•	"situacao"
# 	4.	Ordene a nova lista de forma decrescente pela média de vendas
# 	5.	Exiba os dados formatados no final

vendedores = [
    {"nome": "Carlos", "vendas": [850.50, 910.30, 1000.00]},
    {"nome": "Luciana", "vendas": [400.00, 600.00, 500.00]},
    {"nome": "Bianca", "vendas": [1200.00, 1300.00, 1250.00]},
    {"nome": "Rafael", "vendas": [700.00, 720.00, 710.00]},
    {"nome": "Fernanda", "vendas": [200.00, 300.00, 250.00]},
]

print("Lista inicial com dados de vendas dos vendedores:\n")
for vendedor in vendedores:
    print(vendedor)
    # media = lambda x: sum(vendedor["vendas"])/len(vendedor["vendas"])
    # print(media(vendedor))

media_vendas_situacao = list(
    map(
        lambda x: {
            "nome": x["nome"],
            "media_vendas": f'{(sum(x["vendas"]) / len(x["vendas"])):2.2f}',
            "situação": (
                "excelente"
                if (sum(x["vendas"]) / len(x["vendas"])) >= 1000
                else "bom" if (sum(x["vendas"]) / len(x["vendas"])) >= 700 else "baixo"
            ),
        },
        vendedores,
    )
)

# print("\nA média de vendas e situação dos vendedores é:\n")
# for vendedor in media_vendas_situacao:
#     print(vendedor)

ordenacao_venderos_media_vendas = sorted(
    media_vendas_situacao, key=lambda x: x["media_vendas"], reverse=True
)
print("\nA média de vendas e situação dos vendedores em ordem decrescente é:\n")
for vendedor in ordenacao_venderos_media_vendas:
    print(vendedor)
