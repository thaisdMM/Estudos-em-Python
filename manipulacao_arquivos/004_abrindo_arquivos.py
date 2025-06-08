# Steps For Opening File in Python

# # 1- Find the path of a file
# # We can open a file using both relative path and absolute path. The path is the location of the file on the disk.
# # An absolute path contains the complete directory list required to locate the file.
# # A relative path contains the current directory and then the file name.

# # 2- Decide the access mode
# # The access mode specifies the operation you wanted to perform on the file, such as reading or writing. To open and read a file, use the r access mode. To open a file for writing, use the w mode.

# # 3- Pass file path and access mode to the open() function
# # fp= open(r"File_Name", "Access_Mode"). For example, to open and read: fp = open('sample.txt', 'r')

# # 4- Read content from a file.
# # Next, read a file using the read() method. For example, content = fp.read(). You can also use readline(), and readlines()

# # 5- Write content into the file
# # If you have opened a file in a write mode, you can write or append text to the file using the write() method. For example, fp.write('content'). You can also use the writeine() method.

# # 6- Close file after completing operation
# # We need to make sure that the file will be closed properly after completing the file operation. Use fp.close() to close a file.

## 1- Openning a file in read mode:

# Opening the file with absolute path
file_path = open("/Users/thaismoreira/Desktop/output.txt", "r")
# read file
print(file_path.read())
# Closing the file after reading
file_path.close()

# Opening the file with relative path
try:
    file_path = open("output.txt", "r")
    # Reading the contents of the file and closing
    print(file_path.read())
    file_path.close()
except FileNotFoundError:
    print("File was not found, please check the path.")


# IMPORTANTE: IOError. exceção usada até o Python 2
## # IOError é mantido por compatibilidade; em códigos modernos, prefira FileNotFoundError para erros de arquivo.

try:
    file_path = open("ola.txt", "r")
    print(file_path.read())
    file_path.close()
except IOError:
    print("File not found. Please check the path.")
finally:
    print("Exit")

# 2- Opening a File in Write Mode
# Note: If the file is already present it will truncate the file, which means all the content previously in the file will be deleted, and the new content will be added to the file.

file_path = open("sample2.txt", "w")
# writting content
file_path.write("Open a file in write mode.")

## Opening the file again for reading the content
file_path = open("sample2.txt", "r")

# # Reading the contents of the file and closing
print(file_path.read())
file_path.close()

# 3- Opening a File in Append Mode
# The difference between this and the write mode is that the file’s content will not be truncated or deleted in this mode.

file_path = open("sample2.txt", "a")

## writting append content
file_path.write("\nAppend a new line in append mode.")

## opening the file again for reading the content
file_path = open("sample2.txt", "r")

## reading the content of the file and closing
print(file_path.read())
file_path.close()

# 4- Opening file using with statement

# The with statement simplifies exception handling by encapsulating common preparation and cleanup tasks.
# This also ensures that a file is automatically closed after leaving the block.
# As the file is closed automatically it ensures that all the resources that are tied up with the file are released.

# Consider there are two files ‘sample.txt’ and ‘sample2.txt’ and we want to copy the contents of the first file to the second.

## Opening file
with open("sample.txt", "r", encoding="utf-8") as infile, open(
    "sample2.txt", "w"
) as outfile:
    # read sample.txt and write its content into sample2.txt
    for line in infile:
        outfile.write(line)

# # Opening the file to read the contents
with open("sample2.txt", "r") as file:
    print(file.read())

# 5- Creating a new file with x

try:
    with open("sample3.txt", "x") as file:
        file.write("Creating a new file using x statament.")

    # reading the contents of the new file
    with open("sample3.txt", "r") as file_read:
        print(file_read.read())
except FileExistsError:
    print(f"This file already exists.")

# 6- Opening a File for multiple operations like r+

with open("sample3.txt", "r+") as file:
    # read the contents before writting
    print(file.read())

    # writting a new content to this file
    file.write("\nUsing r+ to adding a new content in the file.")

## 7- Opening a Binary file

# Binary files are basically the ones with data in the Byte format (0’s and 1’s)

# We can open and read the contents of the binary file as below

with open("sample.bin", "wb") as binary_file:
    binary_file.write(b"\x48\x65\x6c\x6c\x6f\x2c\x20\x57\x6f\x72\x6c\x64\x21")

with open("sample.bin", "rb") as binary_file_read:
    byte_content = binary_file_read.read(1)
    while byte_content:
        # printing the content of the file
        print(byte_content)
        byte_content = binary_file_read.read(1)
        # > atualiza a variavel para não dar looping infinito
