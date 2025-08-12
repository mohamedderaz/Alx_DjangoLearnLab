from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Author, Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create author
        self.author = Author.objects.create(name="J.R.R. Tolkien")

        # Create some books
        self.book1 = Book.objects.create(
            title="The Hobbit",
            publication_year=1937,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="The Lord of the Rings",
            publication_year=1954,
            author=self.author
        )

        self.client = APIClient()

        # URLs
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})

    def test_list_books(self):
        """Test retrieving list of books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_create_book_authenticated(self):
        """Test creating a book as authenticated user."""
        self.client.login(username='testuser', password='testpass')
        data = {
            "title": "Silmarillion",
            "publication_year": 1977,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Test creating a book without login fails."""
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2000,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        """Test updating a book."""
        self.client.login(username='testuser', password='testpass')
        data = {
            "title": "The Hobbit - Updated",
            "publication_year": 1937,
            "author": self.author.id
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "The Hobbit - Updated")

    def test_delete_book(self):
        """Test deleting a book."""
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())

    def test_filter_books_by_title(self):
        """Test filtering books by title."""
        response = self.client.get(f"{self.list_url}?title=The Hobbit")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(b['title'] == "The Hobbit" for b in response.data))

    def test_search_books(self):
        """Test searching books."""
        response = self.client.get(f"{self.list_url}?search=Rings")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Rings" in b['title'] for b in response.data))

    def test_order_books_by_publication_year(self):
        """Test ordering books by publication year."""
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [b['publication_year'] for b in response.data]
        self.assertEqual(years, sorted(years))