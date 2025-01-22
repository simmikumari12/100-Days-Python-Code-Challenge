class Library:
    def __init__(self, no_of_books, books):
        self.no_of_books = no_of_books
        self.books = books

    def print_books(self):

        for book in self.books:
            print(f"Printing Book: {book}")

    def add_a_book(self):
        print(f"Adding a book: {self.books}")

    def num_books(self):
        print(f"Number of Books: {self.no_of_books}")

b = Library(12, ["Physcology of Money", "Power of Subconcious Mind"])
b.print_books()