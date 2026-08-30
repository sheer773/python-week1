class Library:
    def __init__(self, books):
        self.books = books
    
    def show_books(self):
        print("Available books:")
        for book in self.books:
            print(f" - {book}")
    
    def borrow_book(self, book_name):
        if(book_name in self.books):
            self.books.remove(book_name)
            print(f"You borrowed {book_name}. Please return in 30 days!")
            return True
        else:
            print(f"{book_name} is not available")
            return False
    
    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"Thanks for returning {book_name}")

class Student:
    def request_book(self):
        return input("Enter book name you want to borrow: ")
    
    def return_book_name(self):
        return input("Enter book name you want to return: ")

# Main program - Menu Driven
lib = Library(["Python", "Java", "C++", "DSA", "DBMS"])
student = Student()

while(True):
    print("\n1.Show Books 2.Borrow 3.Return 4.Exit")
    choice = input("Enter choice: ")
    
    if(choice == "1"):
        lib.show_books()
    elif(choice == "2"):
        book = student.request_book()
        lib.borrow_book(book)
    elif(choice == "3"):
        book = student.return_book_name()
        lib.return_book(book)
    elif(choice == "4"):
        print("Thank you!")
        break
    else:
        print("Invalid choice")