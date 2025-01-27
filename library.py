class Library:
    def __init__(self, books):
        self.books = books
        self.num = len(books)

    def books_info(self):
        print("\nBooks in the Library: ")
        for book in self.books:
            print(f"{book}")
        print(f"Number of Books: {len(self.books)}")

cs = Library(["Comp", "math", "design"])
cs.books_info()