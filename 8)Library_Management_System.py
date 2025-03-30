class Book:
    def __init__(self, book_id, title, author, status="available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status  

    def __str__(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {self.status}"

class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open("books.txt", "r") as file:
                for line in file:
                    book_id, title, author, status = line.strip().split(",")
                    self.books.append(Book(book_id, title, author, status))
        except FileNotFoundError:
            print("No books file found, starting with an empty library.")
        except Exception as e:
            print(f"Error loading books: {e}")

    def save_books(self):
        try:
            with open("books.txt", "w") as file:
                for book in self.books:
                    file.write(f"{book.book_id},{book.title},{book.author},{book.status}\n")
        except Exception as e:
            print(f"Error saving books: {e}")

    def issue_book(self, book_id):
        book = self.search_book(book_id)
        if book and book.status == "available":
            book.status = "issued"
            self.save_books()
            print(f"Book '{book.title}' issued successfully!")
        else:
            print("Sorry, the book is either not available or already issued.")

    def return_book(self, book_id):
        book = self.search_book(book_id)
        if book and book.status == "issued":
            book.status = "available"
            self.save_books()
            print(f"Book '{book.title}' returned successfully!")
        else:
            print("This book is either not found or was not issued.")

    def search_book(self, search_term):
        for book in self.books:
            if str(book.book_id) == str(search_term) or book.title.lower() == search_term.lower():
                return book
        return None

def main():
    library = Library()

    while True:
        print("\nPublic Library Book Management System")
        print("1. Issue Book")
        print("2. Return Book")
        print("3. Search Book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                book_id = int(input("Enter Book ID to issue: "))
                library.issue_book(book_id)
            except ValueError:
                print("Invalid input! Please enter a numeric book ID.")

        elif choice == "2":
            try:
                book_id = int(input("Enter Book ID to return: "))
                library.return_book(book_id)
            except ValueError:
                print("Invalid input! Please enter a numeric book ID.")

        elif choice == "3":
            search_term = input("Enter Book ID or Title to search: ").strip()
            book = library.search_book(search_term)
            if book:
                print(book)
            else:
                print("Book not found.")

        elif choice == "4":
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
