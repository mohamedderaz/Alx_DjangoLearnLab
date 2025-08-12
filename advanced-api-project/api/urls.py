from rest_framework import routers
from django.urls import path, include
from .views import AuthorViewSet, BookViewSet

router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'published_date']
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book-list')

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'published_date']
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')