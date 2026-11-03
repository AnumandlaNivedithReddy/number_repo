'''1'''

# class Students():
#   def __init__(self,name,rollno,marks):
#     self.name=name
#     self.roll_no=rollno
#     self.marks=marks
#   def display(self):
#     print(f"Name:{self.name}\nRoll No:{self.roll_no}\nMarks:{self.marks}\n")
# s1=Students("Nivedith",1,962)
# s2=Students("Reddy",2,100)
# s1.display()
# s2.display()


'''2'''

# class BankAccount():
#     def __init__(self,Name,Balance):
#       self.Name=Name
#       self.Balance=Balance
#     def deposit(self,deposit):
#       if deposit>0:
#         self.Balance+=deposit
#       else :
#         print("Deposit amount should grater than 0")
#       return
#     def withdraw(self,withdraw):
#       if self.Balance>=withdraw:
#         self.Balance-=withdraw
#       else :
#         print("Withdrawl amount is grater than Balance")
#       return
#     def display(self):
#       print(f"Name : {self.Name}\nBalance:{self.Balance}\n")
# A1=BankAccount("Nivedith",1000)
# A1.deposit(-200)
# A1.display()
# A1.withdraw(6000)
# A1.display()


'''3'''
# class Employee():
#   bonus=0
#   Total=0
#   def __init__(self,name,emp_id,basic_salary):
#     self.name=name
#     self.emp_id=emp_id
#     self.basic_salary=basic_salary
#   def calculate_bonus(self):
#     Employee.bonus+=self.basic_salary*0.10
#     Employee.Total+=Employee.bonus+self.basic_salary
#     return
#   def calculate_total_salary(self):
#     self.basic_salary+=Employee.bonus
#     return
#   def display(self):
#     print(f"Employee Name: {self.name}\nEmployee ID: {self.emp_id}\nBasic Salary: {self.basic_salary}\nBonus: {Employee.bonus}\nTotal Salary: {Employee.Total}")
# E1=Employee("Nivedith",)



'''4. Write a bank program in python , which has deposit,withdraw and PIN verification and Check balance features using OOPS.'''


class Bank:
    def __init__(self,Name,Balance,Pin):
        self.name=Name
        self.balance=Balance
        self.pin=Pin
    def Verify_Pin(self,pin):
        if pin==self.pin:
            return True
        else:
            return False
    def Withdraw(self,Amount):
        if Amount <= 0:
            print("Enter a valid amount")
        elif self.balance >= Amount:
            self.balance-=Amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
    def Deposit(self,Amount):
        if Amount>0:
            self.balance+=Amount
            print("Deposit successful")
        else:
            print("Amount should be greater than 0\nDeposit is Failed")
    def Display_Details(self):
        print("Account Holder:",self.name)
        print("Balance:",self.balance)
A1=Bank("Nivedith",1000,1234)
pin=int(input("Enter pin:"))
if A1.Verify_Pin(pin):
    print("PIN Verified Successfully")
    print(f"1. Withdraw\n2. Deposit\n3. Display Details")
    choice=int(input("Enter Your choice:"))
    if choice==1:
      withdraw_Amount=int(input("Enter amount to Withdraw:"))
      A1.Withdraw(withdraw_Amount)
    elif choice==2:
      deposit_Amount=int(input("Enter amount to Deposit:"))
      A1.Deposit(deposit_Amount)
    elif choice==3:
      A1.Display_Details()
    else :
      print("Invalid option")
else:
    print("Invalid PIN")