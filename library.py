import random
import string
from datetime import datetime
from database import get_connection


class Library:

    def __init__(self):
        self.create_tables()

    def gen_id(self, prefix="B"):
        random_id = ""
        for _ in range(5):
            random_id += random.choice(string.ascii_uppercase + string.digits)
        return f"{prefix}-{random_id}"

    def create_tables(self):
        conn = get_connection()
        cursor = conn.cursor()

        # Books Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id VARCHAR(20) PRIMARY KEY,
                title VARCHAR(255),
                author VARCHAR(255),
                copies INT,
                available_copies INT,
                added_on DATETIME
            )
        """)

        # Members Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS members (
                id VARCHAR(20) PRIMARY KEY,
                name VARCHAR(255),
                email VARCHAR(255)
            )
        """)

        # Borrowed Books Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS borrowed_books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                member_id VARCHAR(20),
                book_id VARCHAR(20),
                title VARCHAR(255),
                borrowed_on DATETIME,
                FOREIGN KEY (member_id) REFERENCES members(id),
                FOREIGN KEY (book_id) REFERENCES books(id)
            )
        """)

        conn.commit()
        cursor.close()
        conn.close()

    def add_book(self):
        title = input("Enter title: ")
        author = input("Enter author: ")
        copies = int(input("Enter number of copies: "))

        book_id = self.gen_id()

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO books
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            book_id,
            title,
            author,
            copies,
            copies,
            datetime.now()
        ))

        conn.commit()
        cursor.close()
        conn.close()

        print("Book added successfully.")

    def list_books(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()

        if not books:
            print("No books found.")
        else:
            for b in books:
                print(b)

        cursor.close()
        conn.close()

    def add_member(self):
        name = input("Enter name: ")
        email = input("Enter email: ")
        member_id = self.gen_id("M")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO members
            VALUES (%s, %s, %s)
        """, (member_id, name, email))

        conn.commit()
        cursor.close()
        conn.close()

        print("Member added successfully.")

    def list_members(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM members")
        members = cursor.fetchall()

        if not members:
            print("No members found.")
        else:
            for m in members:
                print(m)

        cursor.close()
        conn.close()
        
        