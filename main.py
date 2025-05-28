from Book import Book
from Ebook import Ebook
from Library import Library

book1 = Book("Kobzar", "Taras Shevchenko", [5, 4, 3])
book2 = Book("Lisova pisnya", "Lesya Ukrainka", [4, 4, 5])
ebook = Ebook("Eneida", "Ivan Kotlyarevskiy", [5, 5, 5], 1.2)

library = Library("Library1")
library.add_book(book1)
library.add_book(book2)
library.add_book(ebook)

print(library.library_average_rating())
print(library.top_rated_book())
