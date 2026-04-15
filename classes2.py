# # more falsafeh on exercise 5 from powerpoint
# class User:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.setAge(age)
#         self.password = "123456"
#         self.login = 0
        
#     def describe(self):
#         if self.age != 0:
#             print(f"user's name is {self.first} {self.last}, and they are {self.age} years old.")
#         else:
#             print(f"user's name is {self.first} {self.last}.")
#     def setPassword(self, password):
#         if len(password) >= 8:
#             self.password = password
#         else:
#             print("lol nope")
#     def setAge(self, age):
#         if age >= 18:
#             self.age = age
#         else:
#             print("haha nope")
#             self.age = 0
#     def incrementLogin(self):
#         self.login += 1
#     def resetLogin(self):
#         self.login = 0
#     def getLogin(self):
#         print(self.login)

# theUser = User("Acheron", "Dalbah", 17)
# theUser.describe()
# theUser.setAge(20)
# theUser.describe()

# newGuy = User("Ahmad", "Dalbah", 20)
# newGuy.incrementLogin()
# newGuy.incrementLogin()
# newGuy.getLogin()
# newGuy.resetLogin()
# newGuy.getLogin()
# # end of falsafeh