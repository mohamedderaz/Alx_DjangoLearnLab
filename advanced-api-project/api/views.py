from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """Full CRUD for Authors. Nested books are included in the serialized output."""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    """Full CRUD for Books. BookSerializer includes validation for publication_year."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# Create your views here.
