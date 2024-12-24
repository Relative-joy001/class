# magic method


class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.pages < other.pages
    
    def __gt__(self, other):
        return self.pages > other.pages
    
    def __add__(self, other):
        return self.pages + other.pages
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.pages
        else:
            raise KeyError(f"Invalid key: '{key}'")

book1 = Book("To Kill a Mockingbird", "Harper Lee", 291)
book2 = Book("1984", "George Orwell", 328)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)


# print(book1)
# print(book1 == book2)
# print(book1 < book3)
# print(book1 > book3)
# print(book1 + book2)

# print("Mockingbird" in book2)

print(book2["pages"])