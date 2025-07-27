from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article

@permission_required('relationship_app.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'relationship_app/article_list.html', {'articles': articles})


@permission_required('relationship_app.can_create', raise_exception=True)
def create_article(request):
    if request.method == 'POST':
        # logic to create article
        ...
    return render(request, 'relationship_app/create_article.html')


@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        # logic to update article
        ...
    return render(request, 'relationship_app/edit_article.html', {'article': article})


@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('article_list')
# Create your views here.
