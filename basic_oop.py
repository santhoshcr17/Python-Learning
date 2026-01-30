class Book:  
    def __init__(self, title, author, page):
        # __init__ is the constructor, runs when a new object is created
        # self = refers to the current object being created
        # Attributes: data stored inside the object
        self.title = title    # Attribute → book's title
        self.author = author  # Attribute → book's author
        self.page = page      # Attribute → number of pages

    def describe(self):
        # Method: an action the object can perform
        # Here it prints details about the book using its attributes
        print("The Book", self.title, "by", self.author, "has", self.page, "pages")

# Create an object (instance) of the Book class
mybook = Book("Harry Potter", "J.K. Rowling", 350)

# Normal way to call the method → Python automatically passes 'mybook' as self
mybook.describe()   # Output: The Book Harry Potter by J.K. Rowling has 350 pages

# Alternate way → call the method from the class and pass the object explicitly
Book.describe(mybook)  # Same output, but here we manually give 'mybook' as self