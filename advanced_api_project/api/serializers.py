from rest_framework import serializers
from .models import Author, Book
import datetime


class BookSerializer(serializers.ModelSerializer):
    """Serializes Book model fields.

    Custom validation:
    - `validate_publication_year` ensures the publication_year is not greater than the current year.
    """

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """Ensure the publication year is not in the future."""
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("publication_year cannot be in the future.")
        return value


class NestedBookSerializer(serializers.ModelSerializer):
    """A simplified Book serializer used for nested representation inside AuthorSerializer.

    We separate this from BookSerializer so nested representations do not require an `author` field
    and remain focused on read/display of related books.
    """

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year']


class AuthorSerializer(serializers.ModelSerializer):
    """Serializes Author objects and includes a nested list of the author's books.

    - `books` is generated via the `related_name='books'` on the Book.author FK.
    - By default this nested list is read-only. If you want to support creating/updating books
      in the same request as the author, see the commented example in `create()` below.
    """

    books = NestedBookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

    # Example: if you wanted to accept nested writes (create books with the author),
    # you would implement create/update to handle nested book data. Here we keep nested
    # books read-only for clarity and safety.
    #
    # def create(self, validated_data):
    #     books_data = validated_data.pop('books', [])
    #     author = Author.objects.create(**validated_data)
    #     for book_data in books_data:
    #         Book.objects.create(author=author, **book_data)
    #     return author