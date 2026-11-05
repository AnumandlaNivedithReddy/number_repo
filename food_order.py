class FoodItem:
    def __init__(self,food_id,name,price,category):
        self.foodid=food_id
        self.name=name
        self.__price=price
        self.category=category
    def get_price(self):
        return self.__price
    def display_details(self):
        print(f"{self.foodid} --> {self.name} ${self.get_price()} {self.category}")
class Restaurant:
    def __init__(self,name,location):
        self.name=name
        self.location=location
        self.menu=[]
    def add_food(self,food):
        self.menu.append(food)
    def display_menu(self):
        print(f"\nWelcome to {self.name} - {self.location}")
        print("========== MENU ==========")
        for food in self.menu:
            food.display_details()
    def find_food(self,food_id):
        for food in self.menu:
            if food.foodid==food_id:
                return food
        return None
class Customer:
    def __init__(self,customer_id,name):
        self.customerid=customer_id
        self.name=name
        self.cart=[]
    def add_to_cart(self,restaurant,food_id):
        food=restaurant.find_food(food_id)
        if food:
            self.cart.append(food)
            print("Item added to cart")
        else:
            print("Food item not found")
    def remove_from_cart(self,food_id):
        for food in self.cart:
            if food.foodid==food_id:
                self.cart.remove(food)
                print("Item removed from cart")
                return
        print("Item not found in cart")
    def view_cart(self):
        if not self.cart:
            print("Your cart is empty")
            return
        print("\n========== YOUR CART ==========")
        for food in self.cart:
            food.display_details()
    def get_discount(self):
        return 5
class PremiumCustomer(Customer):
    def __init__(self,customer_id,name):
        super().__init__(customer_id,name)
    def get_discount(self):
        return 20
class Order:
    def __init__(self,order_id,customer):
        self.orderid=order_id
        self.customer=customer
        self.items=customer.cart.copy()
        self.total=0
        self.discount_amount=0
        self.final_amount=0
    def calculate_total(self):
        for food in self.items:
            self.total+=food.get_price()
        return self.total
    def apply_discount(self):
        discount=self.customer.get_discount()
        self.discount_amount=self.total*discount/100
        self.final_amount=self.total-self.discount_amount
        return self.final_amount
    def generate_bill(self,restaurant):
        print("\n========== FINAL BILL ==========")
        print(f"Restaurant: {restaurant.name}")
        print(f"Customer: {self.customer.name}")
        print(f"Order ID: {self.orderid}")
        print("--------------------------------")
        for food in self.items:
            food.display_details()
        print("--------------------------------")
        print(f"Total Amount: Rs.{self.total}")
        print(f"Discount: Rs.{self.discount_amount}")
        print(f"Discount Rate: {self.customer.get_discount()}%")
        print(f"Final Amount: Rs.{self.final_amount}")
        print("================================")
        self.customer.cart.clear()
I1=FoodItem(1,"Idly",80,"Veg")
I2=FoodItem(2,"Dosa",100,"Veg")
I3=FoodItem(3,"Biryani",250,"Non-Veg")
I4=FoodItem(4,"Pizza",200,"Veg")
R1=Restaurant("Nawab","Hyderabad")
R1.add_food(I1)
R1.add_food(I2)
R1.add_food(I3)
R1.add_food(I4)
print("========== FOOD ORDERING SYSTEM ==========")
customer_id=int(input("Enter Customer ID:"))
customer_name=input("Enter Customer Name:")
print("1. Normal Customer")
print("2. Premium Customer")
customer_type=int(input("Select Customer Type:"))
if customer_type==1:
    C1=Customer(customer_id,customer_name)
elif customer_type==2:
    C1=PremiumCustomer(customer_id,customer_name)
else:
    print("Invalid Customer Type")
    exit()
order_id=1001
while True:
    print("\n========== MAIN MENU ==========")
    print("1. View Restaurant Menu")
    print("2. Add Food to Cart")
    print("3. Remove Food from Cart")
    print("4. View Cart")
    print("5. Place Order")
    print("6. Exit")
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        R1.display_menu()
    elif choice==2:
        R1.display_menu()
        food_id=int(input("Enter Food ID to Add:"))
        C1.add_to_cart(R1,food_id)
    elif choice==3:
        food_id=int(input("Enter Food ID to Remove:"))
        C1.remove_from_cart(food_id)
    elif choice==4:
        C1.view_cart()
    elif choice==5:
        if not C1.cart:
            print("Your cart is empty. Add food first.")
        else:
            O1=Order(order_id,C1)
            O1.calculate_total()
            O1.apply_discount()
            O1.generate_bill(R1)
            order_id+=1
    elif choice==6:
        print("Thank You for choosing our Restaurant!")
        break
    else:
        print("Invalid option. Please try again.")