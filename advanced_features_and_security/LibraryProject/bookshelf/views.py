from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import book

@permission_required('relationship_app.can_view', raise_exception=True)
def book_list(request):
    books = book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})


@permission_required('relationship_app.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # logic to create book
        ...
    return render(request, 'relationship_app/create_book.html')


@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(book, id=book_id)
    if request.method == 'POST':
        # logic to update book
        ...
    return render(request, 'relationship_app/edit_book.html', {'book': book})


@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(book, id=book_id)
    book.delete()
    return redirect('book_list')
# Create your views here.
