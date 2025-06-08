## Steps for Reading a File in Python:

# 1- Find the path of a file
# We can read a file using both relative path and absolute path. The path is the location of the file on the disk.
# An absolute path contains the complete directory list required to locate the file.
# A relative path contains the current directory and then the file name.

# 2- Open file in Read Mode
# To open a file Pass file path and access mode to the open() function. The access mode specifies the operation you wanted to perform on the file, such as reading or writing. For example, r is for reading.
# For example, fp= open(r'File_Path', 'r')

# 3- Read content from a file.
# Once opened, we can read all the text or content of the file using the read() method. You can also use the readline() to read file line by line or the readlines() to read all lines.
# For example, content = fp.read()

# 4- Close file after completing the read operation
# We need to make sure that the file will be closed properly after completing the file operation. Use fp.close() to close a file.

# writting a file for use as example

text = [
    "First line",
    "Second line",
    "Third line",
    "Fourth line",
    "Fifth line",
]
file_path = "/Users/thaismoreira/Desktop/read_demo.txt"

try:
    with open(file_path, "w") as file:
        for line in text:
            file.write(f"{line}\n")
        print(f"File '{file_path}' was created.")
except PermissionError:
    print("You don't have permission to writting this file.")


# 1- Read a Text File
# read file with absolute path

try:
    file = open("/Users/thaismoreira/Desktop/read_demo.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found. Please check the path.")

## 2- Read a File using with statment

# The following are the main advantages of opening a file using ‘with’ statement

# The with statement simplifies exception handling by encapsulating common preparation and cleanup tasks.
# This also ensures that a file is automatically closed after leaving the block.
# As the file is closed automatically it ensures that all the resources that are tied up with the file are released.

file_path = "/Users/thaismoreira/Desktop/read_demo.txt"
# Reading files using 'with'
with open(file_path, "r") as file_read:
    print(file_read.read())


# # 3- File Read Methods

# read()	Returns the entire file content and it accepts the optional size parameter that mentions the bytes to read from the file.
# readline()	The readline() method reads a single line from a file at a time. . Accepts optional size parameter that mentions how many bytes to return from the file.
# readlines()	The readlines() method returns a list of lines from the file.

# 3.1 - readline(): Read a File Line by Line

# a- by default, this method reads the first line in the file.

file_path = "/Users/thaismoreira/Desktop/read_demo.txt"
with open(file_path, "r") as file_read:
    # read first line - readline()
    # assign it to string variable - line
    line = file_read.readline()
    print(line)

# b- Reading First N lines From a File Using readline()

file_path = "/Users/thaismoreira/Desktop/read_demo.txt"
with open(file_path, "r") as file_read:
    # read first 3 lines
    # strip() is because print without space(\n)
    for i in range(3):
        print(file_read.readline().strip())


# c- Reading Entire File Using readline()

# using the while loop
# We need to check whether the pointer has reached the End of the File and then loop through the file line by line.

file_path = "/Users/thaismoreira/Desktop/read_demo.txt"
with open(file_path, "r") as file_read:
    # read the first line
    line = file_read.readline()
    # Iterate the file till it reached the EOF
    while line != "":
        print(line, end="")
        line = file_read.readline()  # atualiza a leitura

# d- Reading First and the Last line using readline()

file_path = "/Users/thaismoreira/Desktop/read_demo.txt"
with open(file_path, "r") as file_read:
    first_line = file_read.readline()
    print(first_line)
    for last_line in file_read:
        # usando o print para entender o que acontece com o last_line no pass, ele armazena o ultimo valor iterado
        # print(f"Last_line no for com pass: {last_line}")
        pass
    print(last_line)

# 3.2- readlines(): Reading File into List

## This method read file line by line into a list.

file_path = "/Users/thaismoreira/Desktop/read_demo.txt"
with open(file_path, "r") as file_read:
    # read files into list
    lines = file_read.readlines()
    print(lines)
    # output: ['First line\n', 'Second line\n', 'Third line\n', 'Fourth line\n', 'Fifth line\n']

# 4- Reading first N lines from a file

## o codigo "head = [next(file_read) for x in range(number_lines)]" usa list comprehension
# for x in range(number_lines) → repete o código dentro do [] 2 vezes (porque number_lines = 2)
# 	•	a cada repetição, ele executa next(file_read) → ou seja, lê a próxima linha do arquivo
# 	•	e coloca esse valor dentro da lista head

file_path = "/Users/thaismoreira/Desktop/read_demo.txt"
number_lines = 2
with open(file_path, "r") as file_read:
    head = [next(file_read) for x in range(number_lines)]
print(head)

# 5- Reading the last N lines in a file
# We can get the last few lines of a file by using the list index and slicing.

file_path = "/Users/thaismoreira/Desktop/read_demo.txt"
n = 2
with open(file_path, "r") as file_read:
    lines = file_read.readlines()[n:]
print(lines)

# 6- Reading N Bytes From The File
# reading the first 30 bytes from the file

file_path = "/Users/thaismoreira/Desktop/read_demo.txt"
try:
    with open(file_path, "r") as file_read:
        print(file_read.read(30))
except FileNotFoundError:
    print("Please check the path.")

# 7- Reading and Writing to the same file

# 'Unsupported Operation' exception

file_path = "/Users/thaismoreira/Desktop/read_demo.txt"
with open(file_path, "r") as file_read:
    print(file_read.read())
    file_read.write("Reading fresh.")
    # output: io.UnsupportedOperation: not writable

# avoid this exception by changing the access mode to r+
# we have to make sure that there is a file existing with the name passed. Otherwise, we will get the FileNotFound exception.

file_path = "/Users/thaismoreira/Desktop/read_demo.txt"
with open(file_path, "r+") as file_read_writte:
    # read from the start
    print(file_read_writte.read())
    # Writing into file
    # write at current position
    file_read_writte.write("\nSixth line")
    # this will read from current file pointer position
    print(file_read_writte.read())
    # write at current position
    file_read_writte.write("\nSeventh line")
    # this will read from current file pointer position
    print(file_read_writte.read())

# 8- Reading File in Reverse Order

file_path = "/Users/thaismoreira/Desktop/read_demo.txt"
with open(file_path, "r") as file_read:
    lines = file_read.readlines()
    for line in reversed(lines):
        print(line)

## 9- Reading a Binary file

file_path = "sample.bin"
with open(file_path, "rb") as binary_file:
    byte_content = binary_file.read(1)
    while byte_content:
        # Printing the contents of the file
        print(byte_content)
        byte_content = binary_file.read(1)
