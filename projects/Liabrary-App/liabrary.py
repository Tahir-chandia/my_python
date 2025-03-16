import json

class Books:
    def __init__(self):
        self.books=[]
        self.storage= "data.json"
        self.read_from()
    
    def read_from(self):
        try:
            with open(self.storage,"r") as file:
                self.books =json.load(file)
        except(FileNotFoundError,json.JSONDecodeError):
            self.books =[]

    def save(self):
        with open(self.storage,"w") as file:
             json.dump(self.books,file,indent=4)
    
    def create_new_book(self):
        """Add a new book to the collection by gathering information from the user."""
        book_title = input("Enter book title: ")
        book_author = input("Enter author: ")
        publication_year = input("Enter publication year: ")
        book_genre = input("Enter genre: ")
        is_book_read = (
            input("Have you read this book? (yes/no): ").strip().lower() == "yes"
        )

        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read,
        }
        self.books.append(new_book)
        self.save()
        print("Book added successfully!\n")

    def remove(self):
        title = input("Enter the title to remove the book. ")
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                self.save()
                print("Book removed")
                return
        print("Book is not found")
        
    def find(self):
        search_term=input("Search by\n1. Title\n2. Author\nEnter your choice: ")
        search_text=input("Enter the text to search: ").lower()
        found_books=[
            book
            for book in self.books
            if search_text in book["title"].lower()
            or search_text in book["author"].lower()
        ]
        if found_books:
            print("Match found")
            for index,book in enumerate(found_books,1):
                status = "Read" if book["read"] else "Unread"
                print(f"{index}-{book["title"]}-{book["author"]}-{book["year"]}-{book["genre"]}-{status}")
        else:
            print("Book does not Matched")


    def update_book(self):
        """Modify the details of an existing book in the collection."""
        book_title = input("Enter the title of the book you want to edit: ")
        for book in self.books:
            if book["title"].lower() == book_title.lower():
                print("Leave blank to keep existing value.")
                book["title"] = input(f"New title ({book['title']}): ") or book["title"]
                book["author"] = (
                    input(f"New author ({book['author']}): ") or book["author"]
                )
                book["year"] = input(f"New year ({book['year']}): ") or book["year"]
                book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]
                book["read"] = (
                    input("Have you read this book? (yes/no): ").strip().lower()
                    == "yes"
                )
                
                self.save()
                print("Book updated successfully!\n")
                return
        print("Book not found!\n")

    def show_all_books(self):
        """Display all books in the collection with their details."""
        if not self.books:
            print("Your collection is empty.\n")
            return

        print("Your Book Collection:")
        for index, book in enumerate(self.books, 1):
            reading_status = "Read" if book["read"] else "Unread"
            print(
                f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
            )
        print()

    def show_reading_progress(self):
        """Calculate and display statistics about your reading progress."""
        total_books = len(self.books)
        completed_books = sum(1 for book in self.books if book["read"])
        completion_rate = (
            (completed_books / total_books * 100) if total_books > 0 else 0
        )
        print(f"Total books in collection: {total_books}")
        print(f"Reading progress: {completion_rate:.2f}%\n")

    def start_application(self):
        """Run the main application loop with a user-friendly menu interface."""
        while True:
            print("📚 Welcome to Your Book Collection Manager! 📚")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for books")
            print("4. Update the book details")
            print("5. View all books")
            print("6. View reading progress")
            print("7. Exit")
            user_choice = input("Please choose an option (1-7): ")

            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.remove()
            elif user_choice == "3":
                self.find()
            elif user_choice == "4":
                self.update_book()
            elif user_choice == "5":
                self.show_all_books()
            elif user_choice == "6":
                self.show_reading_progress()
            elif user_choice == "7":
                self.save()
                print("Thank you for using Book Collection Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    book_manager = Books()
    book_manager.start_application()