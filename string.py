# num=int(input("Enter a number: "))
# if num%2==0:
#     print(f"{num} is an even number")
# else:
#     print(f"{num} is an odd number")
    
    
    
# a=int(input("Enter a number: "))
# b=int(input("Enter another number: "))
# c=int(input("Enter one more number: "))
# if a>b and a>c:
#     print(f"{a} is the largest number") 
# elif b>a and b>c:
#     print(f"{b} is the largest number")
# else:
#   print(f"{c} is the largest number")



# a=10
# b=20
# a,b=b,a
# print(f"After swapping: a={a}, b={b}")




# n = int(input("enter the range: "))
# total = n * (n + 1) //2
# print(f"total={total}")



# num = int(input("Enter Number: "))
# count = 0
# while num > 0:
#     num //= 10
#     count += 1
# print(count)



# def is_armstrong(num):
#   total=0
#   org=num
#   while num!=0:
#     last=num%10
#     total+=last**len(str(org))
#     num//=10
#   return org==total
# num=int(input("Enter The number : "))
# print("yes" if is_armstrong(num) else "no")





# square = (lambda x: x * x)(5)

# print(square)



# def pal(num):
#   num=str(num)
#   return num==num[::-1]
# print("yes" if pal(123321) else "no")


# class Student:
#     start_time="9:30"
#     course="Python"
#     location="Hyderabad"
#     def __init__(self,name,email,gender):
#         self.name=name
#         self.email=email
#         self.g=gender
#     def details(self):
#         print("The name of the student is : ",self.name)
#         print("The gender of the student is : ",self.g)
#         print("the Email Address of the student is : ",self.email)
# s1=Student("Nivedith","nivedith@gmail.com",'M')
# s1.details()
# s2=Student("Shravya","Shravss@gmail.com","F")
# s2.details()


