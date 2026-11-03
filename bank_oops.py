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
Nivedith = Bank("Nivedith", 1000, 1234)
Pavan = Bank("Pavan", 5000, 5678)
Rahul = Bank("Rahul", 3000, 9876)
Account_names={
  "Nivedith" : Nivedith,
  "Pavan":Pavan,
  "Rahul":Rahul
}
holder_name=input("Enter your Account Name:")
holder=Account_names.get(holder_name)
pin=int(input("Enter pin:"))
if holder.Verify_Pin(pin):
    print("PIN Verified Successfully")
    while True:
      print(f"1. Withdraw\n2. Deposit\n3. Display Details\n4. Exit")
      choice=int(input("Enter Your choice:"))
      if choice==1:
        withdraw_Amount=int(input("Enter amount to Withdraw:"))
        holder.Withdraw(withdraw_Amount)
      elif choice==2:
        deposit_Amount=int(input("Enter amount to Deposit:"))
        holder.Deposit(deposit_Amount)
      elif choice==3:
        holder.Display_Details()
      elif choice==4:
        print("Thank You for choosing our Bank")
        break
      else :
        print("Invalid option")
else:
    print("Invalid PIN")