'''1'''


# class Students:
#     def display(self):
#         print("Hello, I am a student")
# s1 = Students()
# s1.display()


'''2'''

# class students():
#   def __init__(self,name,age,marks):
#     self.name=name
#     self.age=age
#     self.marks=marks
#   def display_details(self):
#     print(f"name:{self.name}\nage:{self.age}\nmarks:{self.marks}")
# s1=students("Nivedith",23,962)
# s1.name="Reddy"
# s1.display_details()

'''3'''

# class Calculator():
#   def __init__(self,a,b):
#     self.a=a
#     self.b=b
#   def Addition(self):
#     return self.a+self.b
# c1=Calculator(10,20)
# x=c1.Addition()
# print(x)


'''4'''


# class even_or_odd():
#   def __init__(self,num):
#     self.num=num
#   def EvenorOdd(self):
#     print("yes" if self.num%2==0 else "no")
# eo=even_or_odd(26)
# eo.EvenorOdd()



'''5'''

# class Bank:
#     def __init__(self, customer_name, customer_number, balance=0):
#         self.name = customer_name
#         self.number = customer_number
#         self.amount = balance
#     def deposit(self, deposit_amount):
#         self.amount = self.amount + deposit_amount
#         return self.amount
#     def withdraw(self, withdraw_amount):
#         if withdraw_amount <= self.amount:
#             self.amount = self.amount - withdraw_amount
#             return self.amount
#         else:
#             print("Insufficient balance!")
#             return self.amount
#     def display(self):
#         print("Customer Name:", self.name)
#         print("Customer Number:", self.number)
#         print("Account Balance:", self.amount)
# c1 = Bank("Niv", 1, 1000)
# c1.display()
# print("Balance after deposit:", c1.deposit(500))
# print("Balance after withdrawal:", c1.withdraw(200))



'''6'''
# class Student:
#     def __init__(self, name, roll, branch):
#         self._name = name            
#         self._roll = roll           
#         self._branch = branch       
#     def _displayRollAndBranch(self): 
#         print("Roll:", self._roll)
#         print("Branch:", self._branch)
# class Geek(Student):
#     def displayDetails(self):
#         print("Name:", self._name)  
#         self._displayRollAndBranch() 
# obj = Geek("R2J", 1706256, "IT")
# obj.displayDetails()



# for n in range(2, 10):
#   for d in range(2, n):
#       if n % d == 0:
#           break
#   else:
#       print(n, end=" ")



