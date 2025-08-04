import database

## show all the records
database.show_all()
print("-" * 20)

# add a record to the database
database.add_one("Yuzuriha", "Ogawa", "yuzuhira@stoneage.com")

database.show_all()
print("-" * 20)

# Delete Record use rowid as string
database.delet_one("6")

## Add Many Records

stone_list = [
    ("Tsukasa", "Shishio", "tsukasa@stoneage.com"),
    ("Suika", "Detective", "suika@ishigamevillage.com"),
    ("Kinro", "Gardian", "kinro@ishigamevillage.com"),
]

database.show_all()

database.add_many(stone_list)

## Lookup Email Adrres Record
database.email_lookup("suika@ishigamevillage.com")
