from relationship_app.models import Author, Book, Library, Librarian

author = Author.objects.get(name="author.name")
books = Book.objects.filter(author=author)
print(f"Books: by {author.name}")
for book in books:
    print(f" -{book.title}")


library = Library.objects.get(name="library.name")
books = library.books.all()
print(f"Books in {library.name}: ")
for book in books:
    print(f" -{book.title}").objects.all()


librarian = Librarian.objects.get(library="librarian.name")
library = librarian.library
for librarian in library:
    print(f"Librarian: {librarian.name}) for ({library.name})")