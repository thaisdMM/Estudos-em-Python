import sqlite3

# database in memory, don't save
# connection = sqlite3.connect(":memory:")

## SQLite3 tem apenas 5 DATATYPES:
## NULL
# INTEGER
# REAL -> float
# TEXT
# BLOB -> img, mp3...

# 1 - CONNECT TO A DATABASE

# cria a tabela se ela não existir
connection = sqlite3.connect("customer.db")

# Create a cursor -> para dizer o banco de dados o que vc quer fazer
cursor = connection.cursor()  # cursor() instance

## 2- CREATE A TABLE

## doc string """"""
cursor.execute(
    """ CREATE TABLE customers (
    first_name text,
    last_name text,
    email text
    )"""
)

# Commit our comand
connection.commit()

# Close our connection
connection.close()

## 3- INSERT ONE RECORD INTO TABLE

# cria a tabela se ela não existir
connection = sqlite3.connect("customer.db")

# Create a cursor -> para dizer o banco de dados o que vc quer fazer
cursor = connection.cursor()  # cursor() instance

## Insert data to a Table

# inserindo o valor por vez
cursor.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@codemy.com')")

print("Command executed succesfully...")
# Commit our comand
connection.commit()

# Close our connection
connection.close()

# 4- INSERT MANY RECORDS INTO THE TABLE

# cria a tabela se ela não existir
connection = sqlite3.connect("customer.db")

# Create a cursor -> para dizer o banco de dados o que vc quer fazer
cursor = connection.cursor()  # cursor() instance

many_customers = [
    ("Senku", "Ishigame", "senku@stoneage.com"),
    ("Taiju", "Stone", "senku@stoneage.com"),
    ("Chrome", "Age", "chrome@stoneage.com"),
]

## Insert data to a Table

## Inserir vários valores de uma só vez  -> (?,?,?) a quantidade ? representa cada valor da tabela
cursor.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

print("Command executed succesfully...")
# Commit our comand
connection.commit()

# Close our connection
connection.close()

## 5- QUERY AND FETCHALL

connection = sqlite3.connect("customer.db")

cursor = connection.cursor()

# QUERY the Database

# * tudo
cursor.execute("SELECT * FROM customers")

# cursor.fetchone()
# primeiro ítem
# print(cursor.fetchone())
# print(cursor.fetchone()[0])

# cursor.fetchmany(3)
#  # seleciona os itens como se fosse em tupla, então printa 0,1,2 e exclui 3
# print(cursor.fetchmany(3))

# cursor.fetchall()
# fetchall -> aparece todos os dados
# print(cursor.fetchall())
items = cursor.fetchall()

## 6- FORMAT YOUR RESULTS

print("NAME " + "\t\tEMAIL")
print("-" * 10 + "\t-----------------")
for item in items:
    # print(item)
    # print(item[0])
    # print(item[0] + " " + item[1] + " | " + item[2])
    print(item[0] + " " + item[1] + "\t" + item[2])

connection.commit()

connection.close()

## 7- PRIMARY KEY - unique id

connection = sqlite3.connect("customer.db")

cursor = connection.cursor()

# QUERY the Database

# Primary Key - rowid
cursor.execute("SELECT rowid, * FROM customers")

items = cursor.fetchall()
for item in items:
    print(item)
## com o print do rowid - primary key: no output dá print no rowid
## parte do output:
## (1, 'John', 'Elder', 'john@codemy.com')
## (2, 'Tim', 'Smith', 'tim@codemy.com')

connection.commit()

connection.close()

## 8- USE THE WHERE CLAUSE

connection = sqlite3.connect("customer.db")

cursor = connection.cursor()

# QUERY the Database

# WHERE - pode usar operadores lógicos
# cursor.execute("SELECT * FROM customers WHERE last_name = 'Elder' ")
# cursor.execute(
#     "SELECT * FROM customers WHERE last_name LIKE 'Br%'")
## output: ('Mary', 'Brown', 'mary@codemy.com')
cursor.execute("SELECT * FROM customers WHERE email LIKE '%stoneage.com'")
# #outup:
# ('Senku', 'Ishigame', 'senku@stoneage.com')
# ('Taiju', 'Stone', 'senku@stoneage.com')
# ('Chrome', 'Age', 'chrome@stoneage.com')

items = cursor.fetchall()
for item in items:
    print(item)

connection.commit()

connection.close()

# 9- UPDATE RECORDS

connection = sqlite3.connect("customer.db")

cursor = connection.cursor()

## Update Records

## do jeito abaixo funciona, mas não é correto, pois pode trocar vários dados usando o last_name como referencia
# cursor.execute(
#     """UPDATE customers SET email = 'taiju@stoneage.com'
#                WHERE last_name = 'Stone'"""
# )

## jeito correto para UPDATE e DELETE com o rowid/ primary key
cursor.execute(
    """UPDATE customers SET first_name = 'Bob'
               WHERE rowid = 1"""
)

connection.commit()

# QUERY the Database

cursor.execute("SELECT rowid, * FROM customers")


items = cursor.fetchall()
for item in items:
    print(item)

connection.commit()

connection.close()

## 10- DELETE RECORDS

connection = sqlite3.connect("customer.db")

cursor = connection.cursor()

## Delete com o rowid/ primary key
cursor.execute(
    """DELETE from customers WHERE rowid = 6
"""
)

connection.commit()

# QUERY the Database

cursor.execute("SELECT rowid, * FROM customers")

items = cursor.fetchall()
for item in items:
    print(item)

connection.commit()

connection.close()

# 10- ODER RESULTS

connection = sqlite3.connect("customer.db")

cursor = connection.cursor()

# QUERY the Database - ORDER BY

## DESC descendente - por default é ASC ascendente
# cursor.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
# cursor.execute("SELECT rowid, * FROM customers ORDER BY last_name")
cursor.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")

items = cursor.fetchall()
for item in items:
    print(item)

connection.commit()

connection.close()

# 11- AND/OR

connection = sqlite3.connect("customer.db")

cursor = connection.cursor()

# QUERY the Database - AND/OR

# AND
# cursor.execute("SELECT rowid, * FROM customers WHERE email LIKE '%stoneage.com' AND rowid = 4")
## output: (4, 'Senku', 'Ishigame', 'senku@stoneage.com')
# OR
cursor.execute(
    "SELECT rowid, * FROM customers WHERE email LIKE '%stoneage.com' OR rowid = 4"
)
# outupt:
# (4, 'Senku', 'Ishigame', 'senku@stoneage.com')
# (5, 'Taiju', 'Stone', 'taiju@stoneage.com')

items = cursor.fetchall()
for item in items:
    print(item)

connection.commit()

connection.close()

# 11- LIMITING RESULTS

connection = sqlite3.connect("customer.db")

cursor = connection.cursor()

# QUERY the Database - LIMIT

## LIMIT 2 results
cursor.execute("SELECT rowid, * FROM customers LIMIT 2")

# ## LIMIT 2 results DESC
# cursor.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 3")

items = cursor.fetchall()
for item in items:
    print(item)

connection.commit()

connection.close()

## 12- DELETE(Drop) A TABLE and BACKUPS

connection = sqlite3.connect("customer.db")

cursor = connection.cursor()

# Drop Table -> delet the table customers
cursor.execute("DROP TABLE customers")

connection.commit()

# QUERY the Database

cursor.execute("SELECT rowid, * FROM customers")

items = cursor.fetchall()
for item in items:
    print(item)

connection.commit()

connection.close()
