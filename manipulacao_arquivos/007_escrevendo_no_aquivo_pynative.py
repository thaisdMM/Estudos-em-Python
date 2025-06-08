# Python Write to File using PYNATIVE

# Steps for Writing Data into a File in Python:

# 1- Find the path of a file
# We can read a file using both relative path and absolute path. The path is the location of the file on the disk.
# An absolute path contains the complete directory list required to locate the file.
# A relative path contains the current directory and then the file name.

# 2- Open file in write mode
# Pass file path and access mode w to the open() function. The access mode opens a file in write mode.
# For example, fp= open(r'File_Path', 'w')

# 3- Write content into the file
# Once a file is opened in the write mode, write text or content into the file using the write() method.
# For example, fp.write('new text').
# The write() method will add new text at the beginning of a file. For an existing file, this new content will replace the existing content. If the file is not already present a new file will be created, and content is written into it.

# 4- Close file after completing the write operation
# We need to make sure that the file will be closed properly after completing the file operation. Use fp.close() to close a file.

# 5- Append content at the end of the file
# Pass file path and access mode a to the open() function to open a file in append mode.
# For example, fp= open(r'File_Path', 'a')
# Next, use the write() method to write content at the end of the file without deleting the existing content

# 1- Write to a Text file in Python

text = "This is new content"
# wirittin new content to the file
file_path = open("write_demo.txt", "w")
file_path.write(text)
print("Done Writting.")
file_path.close()

# Open the file for reading the new contents
file_read = open("write_demo.txt", "r")
print(file_read.read())
file_read.close()

# 2- Writing To An Existing File

file_path = "/Users/thaismoreira/GITHUB/Estudos-em-Python/write_demo.txt"

file = open(file_path, "r")
print(file.read())
file.close()

# overwritting  existing  content of a file

file_write = open(file_path, "w")
file_write.write("This is overwritten content.")
file_write.close()

# read file

file_read = open(file_path, "r")
print("Opening file again.")
print(file_read.read())
file_read.close()

# 3- File Write Methods

# writelines(): Write a list of lines to a file
# Use this method when you wanted to write a list into a file.

# without with statement

person_data = ["Name: Emma", "\nAddress: 221 Baker Street", "\nCity: London"]
# writing string and list of lines to a file
fp = open("write_demo1.txt", "w")
fp.writelines(person_data)
fp.close()

# opening the file in read mode
fp = open("write_demo1.txt", "r")
print(fp.read())
fp.close()


# with statement:

file_path = "write_demo2.txt"

person_data = ["Name: Asta", "\nAddress: 221 Villa Hage", "\nCity: Clover Kingdom"]
# writing string and list of lines to a file
with open(file_path, "w") as file:
    file.writelines(person_data)

# opening the file in read mode
with open(file_path, "r") as file_read:
    content = file_read.read()
    print(content)


# 4- with Statement to Write a File

name = "Written using a context manager"
with open("write_demo.txt", "w") as file:
    file.write(name)

# opening the file in read mode to access the file

with open("write_demo.txt", "r") as file_read:
    content = file_read.read()
    print(content)

# 5- Appending New Content to an Existing File
file_path = "write_demo.txt"

name = "\nYuno"
address = ["\nAddress: 221 Hage Street", "\nCity: Clover Kingdom", "\nCountry: Japan"]

# # append to file
# with open(file_path, "a") as file_append:
#     file_append.write(name)
#     file_append.writelines(address)

# # opening the file in read mode to access the file
with open(file_path, "r") as file_read:
    content = file_read.read()
    print(content)

# 6- Append and Read on the Same File

# ERROR: we opened a file two times, one for appending and the second call for a reading.
# If we try to read without opening the file again we will get the Unsupported operation exception.

file_path = "write_demo.txt"

name2 = "Antony\n"
address2 = ["224 Baker Street\n", "London\n"]

with open(file_path, "a") as file_append:
    file_append.write(name2)
    file_append.writelines(address2)
    print(file_append.read())
    ## output: io.UnsupportedOperation: not readable
## It is possible to do both append and read operations together by using the access mode a+


# CORRECT a+

file_path = "write_demo.txt"

name = "\nAntony"
address = ["\nAddress: 221 Baker Street", "\nCity: London", "\nCountry:United Kingdom"]

with open(file_path, "a+") as file_append:
    file_append.write(name)
    file_append.writelines(address)
    # move file handle to the start
    # seek(0) não muda onde a escrita acontece nesse modo.
    # seek(0) muda onde a leitura começa, caso você vá ler o conteúdo.
    file_append.seek(0)
    print(file_append.read())

# w+

# If you want to perform both write and read then change the access mode to w+
# For an existing file, the content will be overwritten

file_path = "write_demo1.txt"

with open(file_path, "w+") as file_write_read:
    file_write_read.write("Noelle")
    # move file handle to the start
    file_write_read.seek(0)
    print(file_write_read.read())


## 7- Writing to a Binary File

file_path = "write_demo.bin"
data = "I like piza!".encode("utf-8")
with open(file_path, "wb+") as binary_file:
    binary_file.write(data)
    binary_file.seek(0)
    content = binary_file.read(1)
    while content:
        print(content)
        content = binary_file.read(1)


# SUGERIR CORREÇÃO AO ADMINISTRADOR DO ARQUIVO

# TypeError: a bytes-like object is required, not 'str'
# file = open("Writedemo.bin", "wb")
# file.write("This is a sample string stored in binary format")
# file.close()
