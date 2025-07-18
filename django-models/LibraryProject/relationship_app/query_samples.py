import os
import django

# إعداد بيئة Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# اسم المؤلف اللي عايز تجيب كتبه
author_name = "Ahmed Khaled Tawfik"

# 1. Query all books by a specific author
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with name {author_name}")

# 2. List all books in a library
try:
    library = Library.objects.get(name="Central Library")
    books_in_library = library.books.all()
    print(f"\nBooks in {library.name}:")
    for book in books_in_library:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print("Library not found.")

# 3. Retrieve the librarian for a library
try:
    librarian = Librarian.objects.get(library=library)
    print(f"\nLibrarian for {library.name}: {librarian.name}")
except Librarian.DoesNotExist:
    print("No librarian found for this library.")