# x=[10, 20, 5, 30]
# x.sort()
# print(x[len(x)-2])

# x=[10, 20, 5, 30]
# y=0
# z=0
# for i in x:
#   if i>y :
#     z=y
#     y=i
# print(z)



# x=[1,2,2,3,4,4]
# y=[]
# for i in x:
#   if i not in y:
#     y.append(i)
# print(y)

# x= "banana"
# y= {}
# for i in x:
#     if i in y:
#         y[i] += 1
#     else:
#         y[i] = 1
# print(y)


# x="swiss"
# y=[]
# z=""
# for i in x:
#   y.append(i)
#   if i not in y:
#     z=i





# from pathlib import Path
# Base_DIR=Path(__file__).resolve().parent
# print(Base_DIR)
# data_DIR=Base_DIR / "data"
# print(data_DIR)
# data_DIR.mkdir(parents=True,exist_ok=True)
# File_PATH=data_DIR / "students.txt"
# print(File_PATH)
# if File_PATH.exists():
#     print("The file is exist")
# else:
#     print("The file is doesnot exist")