from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

@permission_required('relationship_app.can_view', raise_exception=True)
def Book_list(request):
    Books = Book.objects.all()
    return render(request, 'relationship_app/Book_list.html', {'Books': Books})


@permission_required('relationship_app.can_create', raise_exception=True)
def create_Book(request):
    if request.method == 'POST':
        # logic to create Book
        ...
    return render(request, 'relationship_app/create_Book.html')


@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_Book(request, Book_id):
    Book = get_object_or_404(Book, id=Book_id)
    if request.method == 'POST':
        # logic to update Book
        ...
    return render(request, 'relationship_app/edit_Book.html', {'Book': Book})


@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_Book(request, Book_id):
    Book = get_object_or_404(Book, id=Book_id)
    Book.delete()
    return redirect('Book_list')
# Create your views here.
