from relationship_app.models import Author, Book, Library, Librarian


author_name = "name"
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)
print(f"Books: by {author.name}")
for book in books:
    print(f" -{book.title}")


library_name = "name"
library = Library.objects.get(name=library_name)
books = library.books.all()
print(f"Books in {library.name}: ")
for book in books:
    print(f" -{book.title}").objects.all()

librarian_name = "name"
librarian = Librarian.objects.get(library=librarian_name)
library = librarian.library
for librarian in library:
    print(f"Librarian: {librarian.name}) for ({library.name})")