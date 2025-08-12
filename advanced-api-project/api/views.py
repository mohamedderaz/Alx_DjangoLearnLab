from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Book  # أو أي موديل عندك

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'  # حط اسم التمبلت المناسب
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'description']
    template_name = 'book_form.html'

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = '/'  # عدّل الرابط المناسب بعد الحذف