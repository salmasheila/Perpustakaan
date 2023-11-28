class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author}"

    def check_out(self):
        if self.available:
            self.available = False
            return True
        else:
            return False

    def check_in(self):
        self.available = True
