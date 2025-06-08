# Python reading files (.txt, .json, .csv) Bro Code

import json
import csv

# txt

# 1-
file_path = "/Users/thaismoreira/Desktop/output.txt"

with open(file_path, "r") as file:
    content = file.read()
    print(content)

# 2- ERROR FileNotFoundError: [Errno 2] No such file or directory:
> no caso abaixou faltou .txt - agora com a exceção: output: That file was not found.
# tb adicionamos PermissionError

file_path = "/Users/thaismoreira/Desktop/output.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found.")
except PermissionError:
    print("You do not have permission to read tha file.")

# json

file_path = "/Users/thaismoreira/Desktop/employees2.json"
try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print( content)
except FileNotFoundError:
    print("That file was not found.")
except PermissionError:
    print("You do not have permission to read tha file.")

# ## consegue acessar no json com a chave
file_path = "/Users/thaismoreira/Desktop/employees2.json"
try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print( content["name"]) # output: Spongebob
except FileNotFoundError:
    print("That file was not found.")
except PermissionError:
    print("You do not have permission to read tha file.")

# csv

file_path = "/Users/thaismoreira/Desktop/employees3.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
            # # dá para acessar uma coluna específica passando o index
            # print(line[0])
except FileNotFoundError:
    print("That file was not found.")
except PermissionError:
    print("You don't have permission to read this file.")
