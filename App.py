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
                data = json.load(content)        
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
        random_id = " "
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
else :
    print("Wrong Choice!! Please Try Again!!")

