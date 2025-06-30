# # acessing object data

# # class User:
# #     def __init__(self, username, email, passoword):
# #         self.username = username
# #         self.email = email
# #         self.passoword = passoword

# #     def say_hi_to_user(self, user):
# #         print(
# #             f"Sending massage to {user.username}: Hi {user.username},it's {self.username}"
# #         )

# # user1 = User("robynwood", "robyn@gmail.com", "123")
# # user2 = User("batman", "bat@outlook.com", "abc")

# # user1.say_hi_to_user(user2)

# # modifying object data


# class User:
#     def __init__(self, username, email, passoword):
#         self.username = username
#         self.email = email
#         self.passoword = passoword

#     def say_hi_to_user(self, user):
#         print(
#             f"Sending massage to {user.username}: Hi {user.username},it's {self.username}"
#         )


# user1 = User("robynwood", "robyn@gmail.com", "123")

# print(user1.email)  # output: robyn@gmail.com
# user1.email = "rob@gmail.com"
# print(user1.email)  # output: rob@gmail.com
# # dá para mofificar para qualquer informção que quiser e isso não é bom. ex:
# user1.email = "jin"
# print(user1.email) # output: jin

# Acessing and Modifying Data:
# 1- The traditional way: make the data private and use getters and setters:


class User:
    def __init__(self, username, email, passoword):
        self.username = username
        # atributo protegido _ desses antes do nome ex: _email
        self._email = email
        self.passoword = passoword

    def get_email(self):
        return self._email


user1 = User("robynwood", "robyn@gmail.com", "123")
print(user1.email)
