class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []
        
    def add_books(self, newbook):
        self.books.append(newbook)
        self.no_of_books += 1

    def Available_Books(self):
        print(f"There are total {self.no_of_books} book/books available which is/are: ")
        for book in self.books:
            print(book)
# lib1 = Library()
# lib1.add_books("Panchtantra")
# lib1.Available_Books()

Lib_name = input("Welcome to the Library_Management\n What is your Library name? ")
print(f"Welcome to the {Lib_name} Library.")
Lib1 = Library()
while True:
    try:
        opt = input(f"Type 'add' to add a book in library or type 'books' to see the available books in {Lib_name} Library ").strip().lower()
        if opt == "add":
            Book = input("Enter the name of book: ").strip().lower()
            Lib1.add_books(Book)
        elif opt == "books":
            Lib1.Available_Books()
        else:
            print("Invalid option. Please salect the correct option")
    
        cont = input("Do you want to continue? (yes/no): ")
        if cont != "yes":
            print("Exiting the Library Management System. Goodbye!")
            break
    
    except Exception as e:
            print(f"An Error {e} occur. Please try again.")