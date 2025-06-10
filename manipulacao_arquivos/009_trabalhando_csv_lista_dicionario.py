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
#     with open(file_path, "w+") as write_file:
#         writer = csv.writer(write_file)
#         for row in dados:
#             writer.writerow(row)
#         print(f"File {file_path} was created!")
# except FileNotFoundError:
#     print("File csv was not found.")
# except PermissionError:
#     print("You don't have permission to created this file.")

# try:
#     with open(file_path, "r") as read_file:
#         content = csv.reader(read_file)
#         for line in content:
#             print(line)
# except FileNotFoundError:
#     print("File csv was not found.")
# except PermissionError:
#     print("You don't have permission to created this file.")

with open(file_path, "r") as read_file:
    content = csv.reader(read_file)
    for line in content:
        chaves = {(line)[0][:]}
        print(line)
        print(chaves)
print(chaves)