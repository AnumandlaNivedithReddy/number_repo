# def even_or_odd(num):
#   return num%2==0
# print("even" if even_or_odd(12) else "odd")

# def is_prime(num):
#   for i in range(2,num):
#     if num%i==0:
#       return False
#   return True
# print("prime" if is_prime(19) else "not a prime")    

# def is_palindrom(val):
#   val=str(val)
#   return val==val[::-1]
# print("palindro " if  is_palindrom(121) else "not a plaindrom")


from functools import reduce
# def factorial(num):
#   result=reduce(lambda x,y:x*y,range(1,num+1))
#   return result
# print(factorial(2))



# def factorial(num):
#   total=1
#   for i in range(1,num+1):
#     total*=i
#   return total
# print(factorial(400))


# def is_strong(num):
#   total=0
#   for i in str(num):
#     total+=reduce(lambda x,y :x*y,range(1,int(i)+1),1)
#   return total==num
# print("strong" if is_strong(143) else "not a strong")


# def is_armstrong(num):
#   total=0
#   for i in str(num):
#     total+=int(i)**len(str(num))
#   return total==num
# print("armstrong" if is_armstrong(371) else "not a armstrong")


# def is_disaram(num):
#   dig=len(str(num))
#   total=0
#   str_num=str(num)
#   for i in str_num[::-1]:
#     total+=int(i)**dig
#     dig-=1
#   return total==num
# print("disaram" if is_disaram(185) else "not a disaram")


# def is_happy(num):
#   while num!=1:
#     total=0
#     for i in str(num):
#       total+=int(i)**2
#       num=total
#     if total==1:
#       return True
# print("happy" if is_happy(23) else " not happy")