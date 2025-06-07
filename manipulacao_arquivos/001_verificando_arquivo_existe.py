import os

## RELATIVE FILE_PATH

file_path = "test.txt"

if os.path.exists(file_path):
    print(f"This file already existis. The location is: '{file_path}'")
else:
    print("That location doesn't exist.")
# output: This file already existis. The location is: 'test.txt'

# here, the location doesn't exist, we change the txt for pdf
file_path = "test.pdf"

if os.path.exists(file_path):
    print(f"This file already existis. The location is: '{file_path}'")
else:
    print("That location doesn't exist.")

# se eu mudar o arquivo para dentro de uma pasta, como agora dentro da pasta manipulação de arquivo, já que o python entende que o caminho é estudos em python o resultado do terminal dá que o local não existe
# > para o codigo achar agora eu tenho que passar o caminho da pasta:

file_path2 = "manipulacao_arquivos/test.txt"

if os.path.exists(file_path2):
    print(f"This file already existis. The location is: '{file_path2}'")
else:
    print("That location doesn't exist.")
## output: This file already existis. The location is: 'manipulacao_arquivos/test.txt'

# ABSOLUTE FILE_PATH

absolute_file_path = "/Users/thaismoreira/Desktop/test2.txt"

if os.path.exists(absolute_file_path):
    print(f"The location '{absolute_file_path}' exists.")
else:
    print("The location doesn't exist.")
## output: The location '/Users/thaismoreira/Desktop/test2.txt' exists.
# if we change the extension txt to pdf it would print the location doesn't exist.


absolute_file_path = "/Users/thaismoreira/Desktop/test2.pdf"

if os.path.exists(absolute_file_path):
    print(f"The location '{absolute_file_path}' exists.")
else:
    print("The location doesn't exist.")
## output: The location doesn't exist.

# se for um arquivo ou se for uma pasta

absolute_file_path = "/Users/thaismoreira/Desktop/test2.txt"

if os.path.exists(absolute_file_path):
    print(f"The location '{absolute_file_path}' exists.")
    if os.path.isfile(absolute_file_path):
        print("That is a file.")
else:
    print("The location doesn't exist.")
## output:
# The location '/Users/thaismoreira/Desktop/test2.txt' exists.
# That is a file.

# se for uma pasta, mas nao pode colocar o txt

absolute_file_path = "/Users/thaismoreira/Desktop/test2"

if os.path.exists(absolute_file_path):
    print(f"The location '{absolute_file_path}' exists.")
    if os.path.isfile(absolute_file_path):
        print("That is a file.")
    elif os.path.isdir(absolute_file_path):
        print("That is a directory/folder.")
else:
    print("The location doesn't exist.")
# output:
# The location '/Users/thaismoreira/Desktop/test2' exists.
# That is a directory/folder.
