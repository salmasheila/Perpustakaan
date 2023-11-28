class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.checked_out_books = []

    def check_out_book(self, book):
        if book.check_out():
            self.checked_out_books.append(book)
            return True
        else:
            return False

    def return_book(self, book):
        if book in self.checked_out_books:
            book.check_in()
            self.checked_out_books.remove(book)
            return True
        else:
            return False
