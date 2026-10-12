# from functools import reduce
# def decimal_to_binary(n):
#   num=[]
#   while n!=0:
#     reminder=n%2
#     num.append(reminder)
#     n//=2
#   return list(reversed(num))
# result=decimal_to_binary(10)
# output=reduce(lambda x,y:str(x)+str(y),result)
# print(output)

print("for the String")
a = 'Hello' 
b = 'Hello'

print(a is b)

# print(f"ID of a is {id(a)}")
# print(f"ID of b is {id(b)}")


print("for the List")
c = [1,2,3]
d = [1,2,3]

print(c is d)

# print(f"ID of c is {id(c)}")
# print(f"ID of d is {id(d)}")


print("for the tuple")
x = (10,20,30)
y = (10,20,30)

print(x is y)

# print(f"ID of x is {id(x)}")
# print(f"ID of y is {id(y)}")

print("for the Dictionary")
s = {'a':'11', 'b':'22','c':'33'}
t = {'a':'11', 'b':'22','c':'33'}

print(s is t)

# print(f"ID of s is {id(s)}")
# print(f"ID of t is {id(t)}")


print("for the integer")
ax= 99
bx = 99

print(ax is bx)

# print(f"ID of ax is {id(ax)}")
# print(f"ID of bx  is {id(bx)}")


print("for the set")
x = {10,20,30}
y = {10,20,30}

print(x is y)