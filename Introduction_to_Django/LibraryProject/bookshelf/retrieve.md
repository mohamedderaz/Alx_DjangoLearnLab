# retrieve.md

from bookshelf.models import Book

# استرجاع جميع الكتب
book = Book.objects.get(title="1984")
book.title
# '1984'
book.author
# 'George Orwell'
book.publication_year
# 1949
