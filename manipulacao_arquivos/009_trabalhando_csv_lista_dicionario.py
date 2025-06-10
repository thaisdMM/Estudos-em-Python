import csv

dados = [
    ["name", "age", "job"],
    ["Tiago", 45, "motorista"],
    ["Felipe", 41, "desempregado"],
    ["Dulcinéia", 60, "vendedora"],
    ["Marcos", 22, "segurança"],
    ["Lana", 50, "comerciante"],
]
file_path = "dados_pessoas.csv"

try:
    with open(file_path, "w", newline="") as write_file:
        writer = csv.writer(write_file)
        for row in dados:
            writer.writerow(row)
        print(f"File {file_path} was created!")
except FileNotFoundError:
    print("File csv was not found.")
except PermissionError:
    print("You don't have permission to created this file.")

data = {}

try:
    with open(file_path, "r", newline="") as read_file:
        content = csv.reader(read_file)
        cabecalho = next(content)
        for key in cabecalho:
            data[key] = []
        for row in content:
            for i in range(0, len(cabecalho)):
                if cabecalho[i] == "age":
                    data[cabecalho[i]].append(int(row[i]))
                else:
                    data[cabecalho[i]].append(row[i])
except FileNotFoundError:
    print("File csv was not found.")
except PermissionError:
    print("You don't have permission to created this file.")
print(cabecalho)
print(data)
print(f"Total das idades é {sum(data['age'])}")
media_idade = sum(data["age"]) / len(data["age"])
print(media_idade)

# # codigo Téo Me Why - mais simples, "iniciante", não usa as praticas do csv

chaves = dict()

with open(file_path) as file_read:
    content = file_read.readlines()
print(content)

# for line in content:
#     print(line)

dados = dict()

chaves = content[0].strip("\n").split(",")
print(chaves)
for key in chaves:
    dados[key] = []
    # print(dados)
# print(dados)

for line in content[1:]:
    valores = line.strip("\n").split(",")
    # print(valores)
    for i in range(0, len(valores)):
        dados[chaves[i]].append(valores[i])
        # print(dados)
print(dados)

idade = []
for valor in dados["age"]:
    idade.append(int(valor))
print(idade)
media = sum(idade) / len(idade)
print(media)
