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

# class bank():
#   Amount=0
#   def __init__(self,Customer_Name,Customer_Number,add=0,sub=0):
#     self.name=Customer_Name
#     self.number=Customer_Number
#     self.add=add
#     self.sub=sub
#   def deposit(self):
#     amount=amount+self.amount
#     return amount   
#   def withdraw(self):
#     self.amount=self.amount-self.sub
#     return self.amount
# c1=bank("niv",1,)


'''6'''
class Student:
    def __init__(self, name, roll, branch):
        self._name = name            
        self._roll = roll           
        self._branch = branch       
    def _displayRollAndBranch(self): 
        print("Roll:", self._roll)
        print("Branch:", self._branch)
class Geek(Student):
    def displayDetails(self):
        print("Name:", self._name)  
        self._displayRollAndBranch() 
obj = Geek("R2J", 1706256, "IT")
obj.displayDetails()