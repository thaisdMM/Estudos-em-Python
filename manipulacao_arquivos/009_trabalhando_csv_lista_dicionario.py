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

# try:
#     with open(file_path, "w", newline="") as write_file:
#         writer = csv.writer(write_file)
#         for row in dados:
#             writer.writerow(row)
#         print(f"File {file_path} was created!")
# except FileNotFoundError:
#     print("File csv was not found.")
# except PermissionError:
#     print("You don't have permission to created this file.")

nomes = []
idades = []
trabalho = []
data = {}

try:
    with open(file_path, "r", newline="") as read_file:
        content = csv.reader(read_file)
        cabecalho = next(content)
        for key in cabecalho:
            data[key] = []
        for row in content:
            for i in range(0, len(cabecalho)):
                if i == 1:
                    data[cabecalho[i]].append(int(row[i]))
                else:
                    data[cabecalho[i]].append(row[i])

        #     nomes.append(row[0])
        #     idades.append(row[1])
        #     trabalho.append(row[2])
        # # data[key][row].append(row)
        # print(data)

        # print(row)
except FileNotFoundError:
    print("File csv was not found.")
except PermissionError:
    print("You don't have permission to created this file.")

# for key in cabecalho:
#     data[key] = []

# # for line in content[1:]:
#     for i in range(0, len(cabecalho)):
#         data[key][i].append(content[i])

# data["name"] = nomes
# for valor in idades:
#     data["age"].append(int(valor))
# data["job"] = trabalho

print(cabecalho)
print(data)
# print(nomes)
# print(idades)
# print(trabalho)

# value = []
# dados = {}

# for valor in nomes:
#     dados["age"] = [valor]
# #     dados[valor[0]]

# print(dados)

# with open(file_path, "r") as read_file:
#     content = csv.reader(read_file)
#     for line in content:
#         chaves = {(line)[0][:]}
#         print(line)
#         print(chaves)
# print(chaves)

# with open(file_path) as file_read:
#     content = file_read.read()
# print(content)


# # codigo Téo Me Why -

# chaves = dict()

# with open(file_path) as file_read:
#     content = file_read.readlines()
# print(content)

# # for line in content:
# #     print(line)

# dados = dict()

# chaves = content[0].strip("\n").split(",")
# print(chaves)
# for key in chaves:
#     dados[key] = []
#     # print(dados)
# # print(dados)

# for line in content[1:]:
#     valores = line.strip("\n").split(",")
#     # print(valores)
#     for i in range(0, len(valores)):
#         dados[chaves[i]].append(valores[i])
#         # print(dados)
# print(dados)

# idade = []
# for valor in dados["age"]:
#     idade.append(int(valor))
# print(idade)
# media = sum(idade) / len(idade)
# print(media)
