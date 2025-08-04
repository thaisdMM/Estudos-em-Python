import sqlite3

## 1- CRIANDO O BANCO DE DADOS, A TABELA E INSERINDO DADOS NO BANCO DE DADOS

# Connect to database
connection = sqlite3.connect("customer.db")

# Create a cursor
cursor = connection.cursor()

## Create a Table

cursor.execute(
    """ CREATE TABLE customers2 (
    first_name text,
    last_name text,
    email text
    )"""
)
# Commit our command
connection.commit()
print("Table created succesfully!")

many_customers2 = [
    ("Senku", "Ishigami", "senku@stoneage.com"),
    ("Taiju", "Oki", "taiju@stoneage.com"),
    ("Chrome", "Age", "chrome@ishigamivillage.com"),
    ("Kohaku", "Ishigami", "kohaku@ishigamivillage.com"),
    ("Gen", "Asagiri", "mentalist@stoneage.com"),
]

## Insert data to a Table

## Inserir vários valores de uma só vez  -> (?,?,?) a quantidade ? representa cada valor da tabela: firs_name, last_name, email
cursor.executemany("INSERT INTO customers2 VALUES (?,?,?)", many_customers2)

print("Insert many executed succesfully...")

# Commit our command
connection.commit()

## Close our connection
connection.close()

## 2- CRIANDO FUNÇÕES RELACIONADAS AO BANCO DE DADOS E TABELA, PARA SEREM USADOS NO CÓDIGO DO "APP"
## implementing functions to use in our_app


## Query The DB and Return All Records
def show_all():
    # Connect to database
    connection = sqlite3.connect("customer.db")
    # Create a cursor
    cursor = connection.cursor()

    ## Query the Database
    cursor.execute("SELECT rowid, * FROM customers2")
    items = cursor.fetchall()
    for item in items:
        print(item)

    # Commit our command
    connection.commit()
    ## Close our connection
    connection.close()


## Add a New Record to the Table
def add_one(first, last, email):
    connection = sqlite3.connect("customer.db")
    cursor = connection.cursor()

    # Query the Database
    cursor.execute("INSERT INTO customers2 VALUES (?,?,?)", (first, last, email))

    connection.commit()
    connection.close()


def add_many(list):
    connection = sqlite3.connect("customer.db")
    cursor = connection.cursor()

    cursor.executemany("INSERT INTO customers2 VALUES(?,?,?)", (list))

    connection.commit()
    connection.close()


## Delete Record  from table
def delet_one(id):
    connection = sqlite3.connect("customer.db")
    cursor = connection.cursor()

    cursor.execute("DELETE from customers2 WHERE rowid = (?)", id)

    connection.commit()
    connection.close()


## Lookup with Where
def email_lookup(email):
    connection = sqlite3.connect("customer.db")
    cursor = connection.cursor()

    cursor.execute("SELECT rowid, * FROM customers2 WHERE email = (?)", (email,))
    items = cursor.fetchall()

    for item in items:
        print(item)

    connection.commit()
    connection.close()
