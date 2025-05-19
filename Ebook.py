from Book import Book

class Ebook(Book):
    def __init__(self, title, author, ratings, file_size):
        super().__init__(title, author, ratings)
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()}\nFile size: {self.file_size} MB"
