delete_books = Book.objects.get(title = "Nineteen Eighty-Four") 
delete_books.delete()
Book.objects.all()
