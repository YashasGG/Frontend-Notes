class Library:
    def __init__(self):
        self.books = {}  # Dictionary to store book titles and their availability
        self.issued_books = {}  # Dictionary to store student and their issued books

    def add_book(self, title):
        self.books[title] = True  # True indicates the book is available

    def issue_book(self, student, title):
        if title in self.books and self.books[title]:
            if student not in self.issued_books:
                self.issued_books[student] = []
            if len(self.issued_books[student]) < 5:
                self.issued_books[student].append(title)
                self.books[title] = False  # Book is now issued
                print(f"Book '{title}' issued to {student}.")
            else:
                print(f"{student} has already issued 5 books.")
        else:
            print(f"Book '{title}' is not available.")

    def return_book(self, student, title):
        if student in self.issued_books and title in self.issued_books[student]:
            self.issued_books[student].remove(title)
            self.books[title] = True  # Book is now available
            print(f"Book '{title}' returned by {student}.")
        else:
            print(f"{student} does not have the book '{title}' issued.")

    def display_books(self):
        print("Available books:")
        for title, available in self.books.items():
            if available:
                print(title)


