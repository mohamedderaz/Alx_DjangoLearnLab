
from .models import Author, Book, Library, Librarian

# اسم المؤلف اللي عايز تجيب كتبه
author_name = "Ahmed Khaled Tawfik"

# 1. Query all books by a specific author
author_name = "Ahmed Khaled Tawfik"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with name {author_name}")

# استعلام كل الكتب داخل مكتبة معينة
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)  # ← السطر المطلوب إضافته حرفياً
    books_in_library = library.books.all()
    print(f"\nBooks in {library.name}:")
    for book in books_in_library:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"No library found with name {library_name}")

# استعلام أمين المكتبة
try:
    librarian = Librarian.objects.get(library=library)
    print(f"\nLibrarian for {library.name}: {librarian.name}")
except Librarian.DoesNotExist:
    print("No librarian found for this library."))