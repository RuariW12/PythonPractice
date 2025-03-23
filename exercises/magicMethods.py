# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#       They are automatically called by many of Python's built-in operations
#       They allow developers to define or customize the behavior of objects

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self): # converts value into a usable string to print
        return f"{self.title} by {self.author}"

    def __eq__(self, other): # checks if two books are equal based on name and author
        return self.title == other.title and self.author == other.author

    def __lt__(self, other): # less than
        return self.num_pages < other.num_pages

    def __gt__(self, other): # greater than
        return self.num_pages < other.num_pages

    def __add__(self, other): # adds num of pages together
        return self.num_pages + other.num_pages

    def __contains__(self, keyword): # finds a keyword
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        if key == 'author':
            return self.author

book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
book4 = Book("The Hobbit", "J.R.R Tolkien", 310)

book2 = Book("Harry Potter", "J.K Rowling", 223)
book3 = Book("Holes", "A.W Corinne", 172)

print(book1)
print(book1 == book4)

print(book2 < book1)

print("Hobbit" in book1)

print(book1['title'])
print(book2['author'])

