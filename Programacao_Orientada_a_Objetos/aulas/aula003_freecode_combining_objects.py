class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Whoof whoof")


class Owner:
    def __init__(self, name, adress, contact_number):
        self.name = name
        self.adress = adress
        self.phone_number = contact_number


owner1 = Owner("Mary", "122 Springfield Drive", "888-999")
dog1 = Dog("Bruce", "Scottish Terrier", owner1)
dog1.bark()
print(
    f"This is: {dog1.name} it is a {dog1.breed}. His owner is: {dog1.owner.name}. They live at {dog1.owner.adress}. If he is lost, please call {dog1.owner.phone_number}"
)

owner2 = Owner("Michael", "123 Springfield Drive", "888-000")
dog2 = Dog("Freya", "Greyhound", owner2)
print(f"Dog name: {dog2.name} its owner: {dog2.owner.name}")
