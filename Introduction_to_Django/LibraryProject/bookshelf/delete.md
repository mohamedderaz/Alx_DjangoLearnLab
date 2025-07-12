# delete.md

from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# التأكد من الحذف
Book.objects.all()
# <QuerySet []>