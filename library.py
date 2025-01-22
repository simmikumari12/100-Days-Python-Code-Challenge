class Library:
    def __init__(self, no_of_books, books ):
        self.no_of_books = 0
        self.books = []

    def print_books(self, books):
        for book in books:
            print(f"Printing Book: {book}")

    def add_a_book(self, book):
        self.books.append(book)
        print(book)
        self.no_of_books = len(self.books)
         
    def num_books(self):
        print(f"Number of Books: {self.no_of_books}")

b = Library(12, ["Physcology of Money", "Power of Subconcious Mind"])
b.print_books()
b.add_a_book()
print(b)