# Exercício: “Desempenho de Produtos”

# Você recebeu uma lista com dados de produtos de uma loja online. Cada produto tem:
# 	•	nome (str)
# 	•	avaliacoes (lista de notas de 0 a 5)

# Seu desafio:
# 	1.	Calcular a média de avaliação de cada produto.
# 	2.	Atribuir um status:
# 	•	“muito bom” se média >= 4.5
# 	•	“bom” se média >= 3.0
# 	•	“ruim” se < 3.0
# 	3.	Criar uma nova lista com dicionários contendo:
# 	•	nome, média (com 2 casas decimais) e status
# 	4.	Ordenar por média (decrescente)
# 	5.	Usar List Comprehension em vez de map() (você pode tentar reescrever com map() depois para comparação)

produtos = [
    {"nome": "Mouse", "avaliacoes": [4, 5, 5, 4]},
    {"nome": "Teclado", "avaliacoes": [3, 3.5, 2]},
    {"nome": "Monitor", "avaliacoes": [5, 5, 4.5, 5]},
    {"nome": "Cabo HDMI", "avaliacoes": [2, 2.5, 3]},
]

media_avaliacao_produtos = [
    {
        "nome": produto["nome"],
        "media": round(sum(produto["avaliacoes"]) / len(produto["avaliacoes"]), 2),
        "status": (
            "muito bom"
            if (sum(produto["avaliacoes"]) / len(produto["avaliacoes"])) >= 4.5
            else (
                "bom"
                if (sum(produto["avaliacoes"]) / len(produto["avaliacoes"])) >= 3.0
                else "ruim"
            )
        ),
    }
    for produto in produtos
]
# dados_produtos_ordenados = [sorted(x) for x in media_avaliacao_produtos["status"]]
dados_produtos_ordenados = sorted(
    media_avaliacao_produtos, key=lambda x: x["media"], reverse=True
)


# print(media_avaliacao_produtos)
for produto in dados_produtos_ordenados:
    for key, value in produto.items():
        print(f"{key:<5} = {value:>10} |", end="")
    print()
