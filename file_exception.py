try:
  types='''  1.Write
  2.Read
  3.Append
  '''
  print(types)
  choice=int(input("enter your choice:"))
  file_name=input("Enter file name:")
  if choice==1:
    content=input("Enter your content:")
    with open(file_name,"w") as f:
      f.write(content)
      print("Written Successfull")      
  elif choice==2:
      with open(file_name,"r") as f:
        print("==================")
        print(f.read())
        print("==================")
      print("Read Successfull")        
  elif choice==3:
      content=input("Enter your content:")
      with open(file_name,"a") as f:
        f.write("\n"+content)
      print("Appended Successfull")
  else:
    print("Invalid Choice")
except FileNotFoundError:
  print("\nFile is not found Try different file name")
finally:
  print("\n\n*************Thank You*************")