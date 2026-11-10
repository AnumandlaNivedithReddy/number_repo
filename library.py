class Book:
    def __init__(self,BookID,BookName,Author):
        self.id=BookID
        self.name=BookName
        self.author=Author
        self.__availability=True
    def get_availability(self):
        return self.__availability
    def display_details(self):
        print(f"ID:{self.id} -- Name:{self.name} -- Author:{self.author} -- Availability:{self.get_availability()}")
    def issue_book(self):
        if self.__availability == True:
            self.__availability = False
            print("Book issued successfully")
        else:
            print("Book is already issued")
    def return_book(self):
        if self.__availability == False:
            self.__availability = True
            print("Book returned successfully")
        else:
            print("Book is already available")
    
class Library:
  def __init__(self,Library_name):
    self.Lname=Library_name
    self.Books=[]
  def add_book(self,book):
    self.Books.append(book)
    print("Book Added Successfully")
  def display_books(self):
    for i in self.Books:
      i.display_details()
  def search_book(self,book_id):
    for i in self.Books:
      if i.id==book_id:
        i.display_details()
        return
    else:
      print("Book not found")
  def remove_book(self,book_id):
    for i in self.Books:
      if i.id==book_id:
        self.Books.remove(i)
        print("Book Removed Successfully")
        return
    else:
      print("Book not found")
  def issue_book(self,id):
    for i in self.Books:
      if i.id==id:
        i.issue_book()
        return
    else:
      print("Book not avaliable")
  def return_book(self,id):
      for i in self.Books:
          if i.id==id:
              i.return_book()
              return
      print("Book not found")
B1=Book(1,"Brave Potter","Marguerite Siek")
B2=Book(2,"Python","Guido")
B3=Book(3,"Java","James")
B4=Book(4,"Harry Potter","J. K. Rowling")
L1=Library("ANR")
L1.add_book(B1)
L1.add_book(B2)
L1.add_book(B3)
L1.add_book(B4)
# L1.search_book(2)
# L1.search_book(10)
# L1.remove_book(2)
L1.display_books()
# L1.remove_book(10)
# B1=Book(1,"Python","Guido")
# B1.issue_book()
# B1.display_details()
# B1.issue_book()
# B1.return_book()
# B1.display_details()
# L1.issue_book(2)
# L1.issue_book(2)
# L1.return_book(2)
# L1.return_book(2)
# L1.issue_book(10)