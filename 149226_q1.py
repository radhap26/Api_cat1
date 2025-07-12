class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def mark_as_borrowed(self):
        """Mark the book as borrowed"""
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False
    
    def mark_as_returned(self):
        """Mark the book as returned"""
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False
    
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} - {status}"


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        """Borrow a book if it's available"""
        if not book.is_borrowed:
            if book.mark_as_borrowed():
                self.borrowed_books.append(book)
                print(f"Successfully borrowed '{book.title}'")
                return True
        else:
            print(f"Sorry, '{book.title}' is already borrowed")
        return False
    
    def return_book(self, book):
        """Return a borrowed book"""
        if book in self.borrowed_books:
            if book.mark_as_returned():
                self.borrowed_books.remove(book)
                print(f"Successfully returned '{book.title}'")
                return True
        else:
            print(f"You haven't borrowed '{book.title}'")
        return False
    
    def list_borrowed_books(self):
        """List all borrowed books"""
        if not self.borrowed_books:
            print(f"{self.name} has no borrowed books")
        else:
            print(f"\n{self.name}'s borrowed books:")
            for i, book in enumerate(self.borrowed_books, 1):
                print(f"{i}. {book.title} by {book.author}")
    
    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"


def display_menu():
    """Display the main menu"""
    print("\n")
    print("LIBRARY MANAGEMENT SYSTEM")
    print()
    print("1. View all books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. List my borrowed books")
    print("5. Exit")
    print()


def main():
    # Create some sample books
    books = [
        Book("The Great Gatsby", "F. Scott Fitzgerald"),
        Book("To Kill a Mockingbird", "Harper Lee"),
        Book("1984", "George Orwell"),
        Book("Pride and Prejudice", "Jane Austen"),
        Book("The Hobbit", "J.R.R. Tolkien"),
        Book("The Catcher in the Rye", "J.D. Salinger")
    ]
    
    # Create a library member
    member_name = input("Enter your name: ")
    member_id = input("Enter your member ID: ")
    member = LibraryMember(member_name, member_id)
    
    print(f"\nWelcome, {member.name}!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            print("\nAll Books in Library:")
            for i, book in enumerate(books, 1):
                print(f"{i}. {book}")
        
        elif choice == "2":
            print("\nAvailable Books:")
            available_books = [book for book in books if not book.is_borrowed]
            if not available_books:
                print("No books available for borrowing")
            else:
                for i, book in enumerate(available_books, 1):
                    print(f"{i}. {book.title} by {book.author}")
                
                try:
                    book_choice = int(input("Enter the number of the book to borrow: ")) - 1
                    if 0 <= book_choice < len(available_books):
                        member.borrow_book(available_books[book_choice])
                    else:
                        print("Invalid book number")
                except ValueError:
                    print("Please enter a valid number")
        
        elif choice == "3":
            if not member.borrowed_books:
                print("You have no books to return")
            else:
                print("\nYour borrowed books:")
                for i, book in enumerate(member.borrowed_books, 1):
                    print(f"{i}. {book.title} by {book.author}")
                
                try:
                    return_choice = int(input("Enter the number of the book to return: ")) - 1
                    if 0 <= return_choice < len(member.borrowed_books):
                        member.return_book(member.borrowed_books[return_choice])
                    else:
                        print("Invalid book number")
                except ValueError:
                    print("Please enter a valid number")
        
        elif choice == "4":
            member.list_borrowed_books()
        
        elif choice == "5":
            print("Thank you for using the Library Management System!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main() 