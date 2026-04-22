# Library Management System

# Importing neccessary modules
import json
import random
import string
from pathlib import Path
from datetime import datetime

# Defining 'Library' class
class Library :
    # Database 
    database = "library.json"
    
    # Dummy Data
    data = {
        "books" : [],
        "members" : []
    }
    
    # Load existing data to JSON or create new JSON
    if Path(database).exists() :
        with open(database, "r") as f :
            content = f.read().strip()
            if content :
                data = json.loads(content)        
    else :
        with open(database, 'w') as f :
            json.dump(data, f, indent=4)
            
    # Saving data 
    @classmethod
    def save_data(cls) :
        with open(cls.database, 'w') as f :
            json.dump(cls.data, f, indent=4, default= str)
    
        
    # Defining function to generate unique id 
    def gen_id(Prefix="B") :
        random_id = ""
        for i in range(5) :
            random_id += random.choice(string.ascii_uppercase + string.digits)
            
        return Prefix + "-" + random_id

    
    # Defining add function
    def add_book(self) :
        title = input("Enter the title : ")
        author = input("Enter the author : ")
        copies = int(input("Enter the number of copies : "))
        
         # Defining a list names as 'book' to store book's information
        book = {
            "id" : Library.gen_id(),
            "title" : title,
            "author" : author,
            "copies" : copies,
            "available_copies" : copies,
            "added_on" : datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        }
        
        Library.data['books'].append(book)
        Library.save_data()
        
    # Define function to list the books
    def list_books(self) :
        if not Library.data['books'] :
            print(f"Sorry! No Books Found!")
            return
        for b in Library.data['books'] :
            print(f"{b['id']:22} {b['title'][:24]:25} {b['author'][:19]:20} {b['copies']}/{b['available_copies']:>3}")
        print() 
        
    # Define function to add member
    def add_member(self) :
        name = input("Enter the Name : ")
        email = input("Enter the Email : ")
        
        member = {
            "id" : Library.gen_id("M"),
            "name" : name,
            "email" : email,
            "borrowed" : []
        }
        
        Library.data['members'].append(member)
        Library.save_data()
        print("Member Added Successfully!!!!")
        
        
    # Define function to show members
    def list_members(self) :
        if not Library.data['members'] :
            print(f"There are no member!!")
            return
        for m in Library.data['members'] :
            print(f"{m['id']:12} {m['name'][:24]:25} {m['email'][:29]:30} {"This guys has currently : "} {m['borrowed']}")
            print("-"*50) 
            
    # Define function to borrow a book
    def borrow(self) :
        member_id = input("Enter your MemberID : ").strip()
        members = [m for m in Library.data['members'] if m['id'] == member_id]
        if not members :
            print(f"{member_id}!! No such MemberID Found!!")
            return
        member = members[0]
        
        book_id = input("Enter BookID : ").strip()
        books = [b for b in Library.data['books'] if b['id'] == book_id]
        if not books :
            print("Sorry!! Not such book is available!!")
            return
        book = books[0]
        if book['available_copies'] <= 0 :
            print("Sorry, This Book is NOT Available!!!")
            return
        
        borrow_entry =  {
            "book_id" : book['id'],
            "title" : book['title'],
            "borrow_on" : datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        }
        
        member['borrowed'].append(borrow_entry)
        book['available_copies'] -= 1
        Library.save_data()
        print("Book Borrowed Successfully!!!")
    

# Displaying the options 
print("="*50)
print("Library Management System")
print("="*50)
print("-"*50)
print("1. Add Book.")
print("2. List Books.")
print("3. Add Member.")
print("4. List Members.")
print("5. Borrow Book.")
print("6. Return Book.")
print("0. Exit.")
print("-"*50)

# Creating an object of Library class
book = Library()

# Taking choice from the user 
choice = int(input("Enter the choice : "))

# Using if-elif-else condition 
if choice == 1 :
    book.add_book()
elif choice == 2 :
    book.list_books()
elif choice == 3 :
    book.add_member() 
elif choice == 4 :
    book.list_members()  
elif choice == 5 : 
    book.borrow() 
elif choice == 6 :
    book.return_book()
else :
    print("Wrong Choice!! Please Try Again!!")