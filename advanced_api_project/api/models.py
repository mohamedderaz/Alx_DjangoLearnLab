from django.db import models

# Author model stores an author's name.
# An Author can have many Book instances (one-to-many relationship).
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model stores a title, publication year and a foreign key to Author.
# The `author` ForeignKey establishes the one-to-many relationship: an Author may have many Books.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
# Create your models here.
