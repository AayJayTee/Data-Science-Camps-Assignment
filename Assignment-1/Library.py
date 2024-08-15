class Book:
    def __init__(self,title,author,ISBN,status='Available'):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.status = status
        
class Member:
    def __init__(self,mname,member_id):
        self.mname = mname
        self.member_id = member_id
        self.mbooklist = []

    def addbooks(self,bookname):
        self.mbooklist.append(bookname)

    def removebooks(self,bookname):
        self.mbooklist.remove(bookname)

class Librarian:
    def __init__(self,lname,empid):
        self.lname = lname
        self.empid = empid

class Library:
    def __init__(self):
        self.lbooklist = []
        self.memberlist = []

    def register_members(self,member):
        self.memberlist.append(member)

    def lendbooks(self,bookname,member_id):
        if bookname.status == 'Available':
            for i in self.memberlist:
                if i.member_id==member_id:
                    i.addbooks(bookname)
                    bookname.status = 'Borrowed'
                    self.lbooklist.remove(bookname)
                    return
            print("Member is not registered")
        else:
            print("Book is unavailable")


    def returnbooks(self,bookname,member_id): 
        for i in self.memberlist:
            if i.member_id == member_id:
                i.removebooks(bookname)
                bookname.status = 'Available'
                self.lbooklist.append(bookname)
                return
        print("Member is not registered")

    def display_books(self):
        for book in self.lbooklist:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.ISBN}, Status: {book.status}")

    def display_members(self):
        for member in self.memberlist:
            print(f"Name: {member.mname}, Member ID: {member.member_id}, Borrowed Books: {[book.title for book in member.mbooklist]}")

# Create instances of Book
b1 = Book("Percy Jackson", "Rick Riordan", "111111111", "Available")
b2 = Book("Harry Potter", "JK Rowling", "222222222", "Available")

# Create an instance of Member
m1 = Member("Bleh", "AG007")

# Create an instance of Library
library = Library()

# Add books to the library
library.lbooklist.extend([b1, b2])

# Register the member in the library
library.register_members(m1)

# Display initial state
print("Initial Library State:")
library.display_books()
library.display_members()

# Lend books to the member
print("\nLending 'Percy Jackson' and 'Harry Potter' to Bleh:")
library.lendbooks(b1, "AG007")
library.lendbooks(b2, "AG007")

# Display state after lending
print("\nLibrary State After Lending:")
library.display_books()
library.display_members()

# Return one book from the member
print("\nReturning 'Percy Jackson' from Aaron Thomas:")
library.returnbooks(b1, "AG007")

# Display final state
print("\nFinal Library State:")
library.display_books()
library.display_members()
