from django.urls import path,include
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),include('relationship_app.urls')
]