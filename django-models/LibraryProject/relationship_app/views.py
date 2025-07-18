from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import UserProfile

# ✅ Function-based View
def list_books(request):
    books = Book.objects.all()  # <-- مطلوب حسب الاختبار
    return render(request, 'relationship_app/list_books.html', {'books': books})  # <-- المسار الصحيح

# ✅ Class-based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # مسار صحيح للقالب
    context_object_name = 'library'
    def check_role(role):
    def has_role(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role

@login_required
@check_role('Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@check_role('Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@check_role('Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Create your views here.
