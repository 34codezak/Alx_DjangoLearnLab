from bookshelf.models import Book

# Delete the book instance
book.delete()
# Verify deletion by trying to retrieve all books
books = Book.objects.all()
print(books)
