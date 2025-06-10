# Python writing files (.txt. .json, .csv)

import json
import csv

# 1- TXT

txt_data = "I like pizza!"

file_path = "output.txt"

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}' was created!")

## ABSOLUTE FILE_PATH
txt_data = "Absolute: I like pizza!"

absolute_file_path = "/Users/thaismoreira/Desktop/output.txt"

with open(absolute_file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file '{absolute_file_path}' was created!")

txt_data = "Absolute: I like pizza!"

absolute_file_path = "/Users/thaismoreira/Desktop/output.txt"
# se rodar com x e já tiver o arquivo dá erro, por isso colocar o tratamento de erro try except
#  FileExistsError: [Errno 17] File exists: '/Users/thaismoreira/Desktop/output.txt'
try:
    with open(absolute_file_path, "x") as file:
        file.write(txt_data)
        print(f"txt file '{absolute_file_path}' was created!")
except FileExistsError:
    print("That file already exists!")

##  a append - cada vez que  roda ele vai dando append no texto

txt_data = "Absolute: I like pizza!"

absolute_file_path = "/Users/thaismoreira/Desktop/output.txt"
# se rodar com x e já tiver o arquivo dá erro, por isso colocar o tratamento de erro try except
#  FileExistsError: [Errno 17] File exists: '/Users/thaismoreira/Desktop/output.txt'
try:
    with open(absolute_file_path, "a") as file:
        file.write("\n" + txt_data)
        print(f"txt file '{absolute_file_path}' was created!")
except FileExistsError:
    print("That file already exists!")

# # essa operação abaixo gera um ERRO: TypeError: write() argument must be str, not list

# employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

# file_path = "/Users/thaismoreira/Desktop/employees.txt"
# try:
#     with open(file_path, "w") as file:
#         file.write(employees)
#         print(f"txt file '{file_path}' was created.")
# except FileExistsError:
#     print("That file already exists!")

# corrigindo o erro da operação:

employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

file_path = "/Users/thaismoreira/Desktop/employees.txt"
try:
    with open(file_path, "w") as file:
        for employee in employees:
            file.write(employee + "\n")
            # colocar o "\n" ou " " para não colar um nome no outro
        print(f"txt file '{file_path}' was created.")
except PermissionError:
    print("You don't have permission to acess this file!")

# JSON
# tem que importar json
# dump() metodo convert our dictionary in json str


employee = {"name": "Spongebob", "age": 30, "job": "cook"}

file_path = "/Users/thaismoreira/Desktop/employees2.json"
try:
    with open(file_path, "w") as file:
        # json.dump(employee, file)
        # # {"name": "Spongebob", "age": 30, "job": "cook"}
        # se quiser identato tem que passar o argumento indent= e quantos espaços vc quer
        json.dump(employee, file, indent=4)
        print(f"json file '{file_path}' was created.")
except PermissionError:
    print("You don't have permission to acess this file!")
# {
#     "name": "Spongebob",
#     "age": 30,
#     "job": "cook"
# }

## csv - coma separate values
## tem que import csv

employees = [
    ["Name,", "Age", "Job"],
    ["Asta", 16, "MagicKnight"],
    ["Yuno", 16, "MagicKnight"],
    ["Noelle", 16, "MagicKnight"],
]

file_path = "/Users/thaismoreira/Desktop/employees3.csv"
try:
    # ele fala que wiriter() metodo cria linhas vazias entre cada row, mas no meu caso isso não aconteceu
    ## se fosse para concertar isso teria que passar newline=""
    # with open(file_path, "w", newline="") as file:
    # > mesmo nao aparecendo no meu, é mais seguro para csv sempre passar esse parametro: newline=""
    ##> Sempre deve ser seguro especificar newline='', já que o módulo csv faz seu próprio tratamento de nova linha (universal)
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created or overwritting.")
except PermissionError:
    print("You don't have permission to acess this file!")
