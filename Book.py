class Book:
    def __init__(self, title, author, ratings):
        self.title = title
        self.author = author
        self.ratings = ratings

    def average_rating(self):
        avg = sum(self.ratings) / len(self.ratings)
        return f"Average rating: {avg}"

    def __str__(self):
        return f"Book title: {self.title}\nAuthor: {self.author}\nRatings: {self.ratings}"

    def ratings_greater_than(self, number):
        formula = [i for i in self.ratings if i > number]
        return f"All ratings greater than {number}: {formula}"

