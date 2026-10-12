from functools import reduce
def reverse_numbe(n):
  rev=[]
  while n!=0:
    new=n%10
    rev.append(new)
    n//=10
  return rev
result=reverse_numbe(123)
output=reduce(lambda x,y:str(x)+str(y),result)
print(int(output))  
