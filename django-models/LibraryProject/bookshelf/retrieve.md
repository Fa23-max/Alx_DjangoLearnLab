from bookshelf.models import Book
books = Book.objects.get(title = "1984")
books.title 
books.author 
books.publication_year 