from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

# List + Create
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


# Retrieve + Update + Delete
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
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
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # إضافة الفلاتر والبحث والترتيب
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # الفلاتر (filter=)
    filterset_fields = ['title', 'author__name', 'publication_year']

    # البحث (search=)
    search_fields = ['title', 'author__name']

    # الترتيب (ordering=)
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # ترتيب افتراضي

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]