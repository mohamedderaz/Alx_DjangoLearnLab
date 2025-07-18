from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm

# ✅ Function-based View
def list_books(request):
    books = Book.objects.all()  # <-- مطلوب حسب الاختبار
    return render(request, 'relationship_app/list_books.html', {'books': books})  # <-- المسار الصحيح

# ✅ Class-based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # مسار صحيح للقالب
    context_object_name = 'library'

# Create your views here.
