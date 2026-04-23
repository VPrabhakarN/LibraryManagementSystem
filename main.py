from library import Library


def menu():
    lib = Library()

    while True:
        print("\n" + "=" * 50)
        print("Library Management System")
        print("=" * 50)
        print("1. Add Book")
        print("2. List Books")
        print("3. Add Member")
        print("4. List Members")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            lib.add_book()
        elif choice == "2":
            lib.list_books()
        elif choice == "3":
            lib.add_member()
        elif choice == "4":
            lib.list_members()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()