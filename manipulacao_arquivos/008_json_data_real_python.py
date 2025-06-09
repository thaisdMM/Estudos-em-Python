# # Inside the JSON object, you can define zero, one, or more key-value pairs. If you add multiple key-value pairs, then you must separate them with a comma (,).

# # A key-value pair in a JSON object is separated by a colon (:). On the left side of the colon, you define a key. A key is a string you must wrap in double quotes ("). Unlike Python, JSON strings don’t support single quotes (').

## Instead of using True or False in title case, you must use the lowercase true or false.

## The JSON standard doesn’t allow any comments, trailing commas(virgula no final do array), or single quotes for strings.

## you can conveniently convert Python data types into JSON (serialization) data and the other way around (deserialization)

import json

## 1- Writing JSON With Python - dumps()

## 1.1- Convert Python Dictionaries to JSON - serialization

food_shopping = {"eegs": 15, "milk": 3}
# when you use .dumps(), you get a Python string in return
# you don't create any kind of JSON data type
json.dumps(food_shopping)
print(food_shopping)
print(type(food_shopping))

# Using json.dumps() gets more interesting when your Python dictionary doesn’t contain strings as keys or when values don’t directly translate to a JSON format:

numbers_present = {1: True, 2: True, 3: False}
print(numbers_present)
# output: {1: True, 2: True, 3: False}
nunbers_json = json.dumps(numbers_present)
# convertendo para o formato json
print(nunbers_json)
## Note: When you convert a dictionary to JSON, the dictionary keys will always be strings in JSON.
# output: {"1": true, "2": true, "3": false}

## The cool thing about Python’s json module is that it takes care of the conversion for you.

dog_id = 1
dog_name = "Frieda"
dog_registry = {dog_id: {"name": dog_name}}
print(dog_registry)
# output: {1: {'name': 'Frieda'}}
convert_registry_json = json.dumps(dog_registry)
print(convert_registry_json)
# json output: {"1": {"name": "Frieda"}}

fazer = ["limpar", "cozinhar", "ler"]
print(fazer)
# output: ['limpar', 'cozinhar', 'ler']
json_fazer = json.dumps(fazer)
print(json_fazer)
# output: ["limpar", "cozinhar", "ler"]

# You can’t use dictionaries, lists, or tuples as JSON keys
## tuple ERRROR: TypeError: keys must be str, int, float, bool or None, not tuple
available_nums = {(1, 2): True, 3: False}
# json.dumps(available_nums)
# print(available_nums)
# output: TypeError: keys must be str, int, float, bool or None, not tuple

## When you set skipkeys in json.dumps() to True, then Python skips the keys that are not supported and would otherwise raise a TypeError - mas perde dados, deve ser usado com cautela
convert_available_nums = json.dumps(available_nums, skipkeys=True)
print(convert_available_nums)
# output: {"3": false}

# you can sort the dictionary keys by setting the sort_keys parameter to True - sorts the keys alphabetically

toy_conditions = {"chew bone": 7, "ball": 3, "sock": -1}
json_toy_conditions = json.dumps(toy_conditions, sort_keys=True)
print(json_toy_conditions)
# output: {"ball": 3, "chew bone": 7, "sock": -1}

# 2- Write a JSON File With Python - dump()

# The json.dump() function has two required arguments:

# The object you want to write
# The file you want to write into

dog_data = {
    "name": "Frieda",
    "is_dog": True,
    "hobbies": [
        "eating",
        "sleeping",
        "barking",
    ],
    "age": 8,
    "address": {
        "work": None,
        "home": (
            "Berlin",
            "Germany",
        ),
    },
    "friends": [
        {
            "name": "Philipp",
            "hobbies": [
                "eating",
                "sleeping",
                "reading",
            ],
        },
        {
            "name": "Mitch",
            "hobbies": [
                "running",
                "snacking",
            ],
        },
    ],
}
file_path = "dogs_data.json"

with open(file_path, "w", encoding="utf-8") as write_file:
    json.dump(dog_data, write_file, indent=4)
    print(f"File '{file_path}' was created")

# reading the content of the file
with open(file_path, "r") as read_file:
    content = json.load(read_file)
    print(content)
## reading by key
with open(file_path, "r") as read_file:
    content = json.load(read_file)
    print(content["hobbies"])

# 3-  Reading JSON With Python - deserialization

# json.loads(): To deserialize a string, bytes, or byte array instances
# json.load(): To deserialize a text file or a binary file

# Note: Deserialization is not the exact reverse of the serialization process. The reason for this is that JSON keys are always strings, and not all Python data types can be converted to JSON data types. This discrepancy means that certain Python objects may not retain their original type when serialized and then deserialized.

# 3.1- Convert JSON Objects to a Python Dictionary

dog_id = 1
dog_name = "Frieda"
dog_registry = {dog_id: {"name": dog_name}}
convert_dog_registry_json = json.dumps(dog_registry)
print(convert_dog_registry_json)
# output: {"1": {"name": "Frieda"}}

deserialization_dog_registry = json.loads(convert_dog_registry_json)
print(deserialization_dog_registry)

## In JSON, the keys must always be strings
## When you used json.loads(), there was no way for Python to know that the string key should be an integer again.
##>  That’s why your dictionary key remained a string after deserialization.
print(deserialization_dog_registry == dog_registry)
# output: False
print(deserialization_dog_registry)
# output: {'1': {'name': 'Frieda'}} > '1'=str
print(dog_registry)
# output: {1: {'name': 'Frieda'}} > 1=int

# 3.2- Deserialize JSON Data Types

dog_data = {
    "name": "Frieda",
    "is_dog": True,
    "hobbies": [
        "eating",
        "sleeping",
        "barking",
    ],
    "age": 8,
    "address": {
        "work": None,
        "home": (
            "Berlin",
            "Germany",
        ),
    },
}

serialization_dog_data = json.dumps(dog_data)
# print(serialization_dog_data)

deserialization_dog_data = json.loads(serialization_dog_data)
# print(deserialization_dog_data)

## When you serialize a Python tuple, it becomes a JSON array. When you load JSON, a JSON array correctly deserializes into a list
print(dog_data == deserialization_dog_data)
print(dog_data)
print(deserialization_dog_data)
# # output: > original data has a tuple, deserialization data has a list
# False
# {'name': 'Frieda', 'is_dog': True, 'hobbies': ['eating', 'sleeping', 'barking'], 'age': 8, 'address': {'work': None, 'home': ('Berlin', 'Germany')}}
# {'name': 'Frieda', 'is_dog': True, 'hobbies': ['eating', 'sleeping', 'barking'], 'age': 8, 'address': {'work': None, 'home': ['Berlin', 'Germany']}}

print(type(dog_data["address"]["home"]))
# ouput: <class 'tuple'>
print(type(deserialization_dog_data["address"]["home"]))
# output: <class 'list'>


# 3.3- Open an External JSON File With Python

# the file already exists

dog_data = {
    "name": "Frieda",
    "is_dog": True,
    "hobbies": [
        "eating",
        "sleeping",
        "barking",
    ],
    "age": 8,
    "address": {
        "work": None,
        "home": (
            "Berlin",
            "Germany",
        ),
    },
    "friends": [
        {
            "name": "Philipp",
            "hobbies": [
                "eating",
                "sleeping",
                "reading",
            ],
        },
        {
            "name": "Mitch",
            "hobbies": [
                "running",
                "snacking",
            ],
        },
    ],
}

file_path = "hello_frieda.json"

with open(file_path, "w", encoding="utf-8") as write_file:
    json.dump(dog_data, write_file, indent=4)
    print(f"File '{file_path}' was created.")

with open(file_path, "r") as read_file:
    content = json.load(read_file)
    print(content)
    print(type(content))
    print(content["name"])

## 4- Interacting With JSON

## 4.1- Prettify JSON With Python

## the default value for indent is None
## The indent parameter works exactly the same for json.dump() as it does for json.dumps()
# Start by trying out json.dumps() with different indentation levels:

dog_friend = {
    "name": "Mitch",
    "age": 6.5,
}
## usar indent para tornar mais facil de ler e editar
print(json.dumps(dog_friend))
print(json.dumps(dog_friend, indent=0))
print(json.dumps(dog_friend, indent=-2))
print(json.dumps(dog_friend, indent=""))
print(json.dumps(dog_friend, indent="→"))
print(json.dumps(dog_friend, indent=2))
print(json.dumps(dog_friend, indent=4))
with open("dog_friend.json", "w") as write_file:
    json.dump(dog_friend, write_file, indent=4)
    print(f"File json was created.")


## 4.2- Validate JSON in the Terminal
## To swiftly check if a JSON file is valid, you can leverage Python’s json.tool. You can run the json.tool module as an executable in the terminal using the -m switch
## json.tool only reports the first error. So you may need to go back and forth between fixing a JSON file and running json.tool.

## example on the shell:
# # python3 -m json.tool dog_frien.json
## Expecting ',' delimiter: line 3 column 5 (char 26)
