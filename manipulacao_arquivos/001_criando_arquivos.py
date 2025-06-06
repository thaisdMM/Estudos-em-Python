import os
from datetime import datetime

# 1- create a empty text file
# in current directory
fp = open("sales.txt", "x")
fp.close()

# no meu caso não cria dentro da pasta que está esse arquivo.py
# Mas o VS Code está executando a partir da pasta Estudos-em-Python (a raiz que você abriu no VS Code)
# Portanto, quando você usa apenas "sales.txt", o Python cria o arquivo em Estudos-em-Python, porque é esse o diretório de execução e não em manipulacao_arquivos que é a pasta do meu codigo
# se eu quisese criar dentro dessa pasta especfifca, teria que passar o caminho relativo na criação como:
# fp = open("manipulacao_arquivos/sales.txt", "x")
# fp.close()


# 2- Open a file only for exclusive creation. If the file already exists, this operation fails.
# ERROR
#  fp = open("sales.txt", "x")FileExistsError: [Errno 17] File exists: 'sales.txt'

# 3- create a empty text file
# Create a new file for writing. If a file already exists, it truncates the file first. Use to create and write content into a new file.

fp = open("sales_2.txt", "w")
fp.write("firs line file")
fp.close()


# import os to check file path

# 4- list files from a working directory
print(os.listdir())
# respota do terminal:
# ['.DS_Store', 'LICENSE', 'manipulacao_arquivos', 'sales.txt', 'sales_2.txt', '.gitattributes', '.git']

# 5- verify file exist
print(os.path.isfile("sales.txt"))
# terminal:
# True

# 6- create a text file for writing using the absolute path
with open(
    "/Users/thaismoreira/GITHUB/Estudos-em-Python/manipulacao_arquivos/profit.txt", "w"
) as fp:
    fp.write("This is the first line, my absolute path")
    pass

##7- verify result using the absolute path
# list files a directory
print(os.listdir("/Users/thaismoreira/GITHUB/Estudos-em-Python/manipulacao_arquivos"))

# output-TERMINAL ['001_criando_arquivos.py', 'profit.txt']

# verify file exist
print(
    os.path.isfile(
        "/Users/thaismoreira/GITHUB/Estudos-em-Python/manipulacao_arquivos/profit.txt"
    )
)
# output True


# 8- join directory path and file name to create file at the specified location
# os.path.join()
# This function accepts the directory path and file name as arguments and constructs an absolute path to create a file

# Specify the directory path
path = "/Users/thaismoreira/Desktop"
file_name = "revenue.txt"

# Creating a file at specified folder
# join directory and file path
with open(os.path.join(path, file_name), "w") as fp:
    # uncomment below line if you want to create an empty file
    fp.write(
        "This is a new line, I had join path and file name, to create a file at my descktop"
    )

# 9- Create a File If Not Exists - hava two ways:
# Use os.path.exists("file_path") function to check if a file exists.
# Use the access mode x in the open() function and  exception handling.

## Example 1: create file if not exists.
file_path = (
    "/Users/thaismoreira/GITHUB/Estudos-em-Python/manipulacao_arquivos/profit.txt"
)
if os.path.exists(file_path):
    print("File already exists")
else:
    with open(file_path, "w") as fp:
        fp.write("This is the first line!")

# Example 2: Use file access mode x
# The access mode x open a file for exclusive creation. If the file already exists, this operation fails with FileExistsError. Use try-except block to handle this error.
try:
    file_path = (
        "/Users/thaismoreira/GITHUB/Estudos-em-Python/manipulacao_arquivos/profit.txt"
    )
    # create file
    with open(file_path, "x") as fp:
        pass
except:
    print("File already exists")


# #10- Create File with a DateTime - Use the datetime module
# from datetime import datetime
# First, get the current datetime value
# Next, we need to format datetime into a string to use it as a file name.
# At last, pass it to the open() function to create a file


# get current date and time
day = datetime.now()
# print(day)
# 1- create a file with date as a name day-month-year
file_name = day.strftime("%d-%m-%Y.txt")
# print(file_name)
with open(file_name, "w") as fp:
    print(f"created: {file_name}")

# #2- with name as day-month-year-hours-minutes-seconds
file_name_2 = day.strftime("%d-%m-%Y-%H-%M-%S.txt")
# print(file_name_2)
with open(file_name_2, "w") as fp:
    print(f"Created: {file_name_2}")

# #3- at specified directory
file_name_3 = "/Users/thaismoreira/Desktop/" + day.strftime("%d-%m-%Y-%H-%M-%S.txt")
# print(file_name_3)
with open(file_name_3, "w") as fp:
    print(f"Created: {file_name_3}")

##11- Create a file with Permission

# To create a file with appropriate permissions, use os.open() to create the file descriptor and set the permission.
# Next, open the descriptor using the built-in function open()

file_path = (
    "/Users/thaismoreira/GITHUB/Estudos-em-Python/manipulacao_arquivos/sample.txt"
)
# # The default umask is 0o22 which turns off write permission of group and others
os.umask(0)
with open(os.open(file_path, os.O_CREAT | os.O_WRONLY, 0o777), "w") as fh:
    fh.write("Content")
