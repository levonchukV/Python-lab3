class Library:
    def __init__(self, library_name, books=None):
        self.library_name = library_name
        self.books = books if books is not None else []

    def add_book(self, book):
        self.books.append(book)

    def library_average_rating(self):
        if not self.books:
            return "No books in the library."

        total_ratings = []
        for book in self.books:
            total_ratings.extend(book.ratings)

        avg = sum(total_ratings) / len(total_ratings)
        return f"Library average rating: {avg}"

    def top_rated_book(self):
        if not self.books:
            return "No books in the library."

        top_book = max(self.books, key=lambda book: sum(book.ratings) / len(book.ratings))
        return f"Top rated book:\n{top_book}"
