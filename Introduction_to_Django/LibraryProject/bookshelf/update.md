# update.md

from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# التأكد من التحديث
book.title
# 'Nineteen Eighty-Four'