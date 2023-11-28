from book import Book
from library import Library
from member import Member

# Buat beberapa buku
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "789012")
book3 = Book("1984", "George Orwell", "345678")

# Tambahkan buku ke perpustakaan
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Tampilkan daftar buku di perpustakaan
print("Books in the library:")
library.display_books()

# Buat anggota perpustakaan
member = Member("John Doe", "M001")

# Peminjaman buku oleh anggota
selected_book = library.search_book("The Great Gatsby")
if selected_book:
    if member.check_out_book(selected_book):
        print(f"{member.name} has checked out {selected_book}")
    else:
        print("Book is not available.")
else:
    print("Book not found in the library.")

# Tampilkan buku yang dipinjam oleh anggota
print(f"\nBooks checked out by {member.name}:")
for checked_book in member.checked_out_books:
    print(checked_book)
