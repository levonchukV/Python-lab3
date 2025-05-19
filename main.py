from Book import Book
from Ebook import Ebook


book = Book("title", "author", [5, 4, 3, 5])
print(book.average_rating())
print(book)
print(book.ratings_greater_than(3))
print("\n" + "-------------------" + "\n")


ebook = Ebook("E-Book", "E-Author", [4, 5, 5, 4], 2.5)
print(ebook.average_rating())
print(ebook)
print(ebook.ratings_greater_than(4))

