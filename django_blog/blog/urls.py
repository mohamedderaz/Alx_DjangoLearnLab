from django.urls import path
from .views import (
    BlogLoginView, BlogLogoutView, register, profile,
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
)

urlpatterns = [
    # Auth
    path('login/',  BlogLoginView.as_view(), name='login'),
    path('logout/', BlogLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/',  profile, name='profile'),

    # === CRUD routes required by the checker (singular 'post/') ===
    path('post/new/',                PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/',    PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/',    PostDeleteView.as_view(), name='post-delete'),

    # Read
    path('',                         PostListView.as_view(),   name='post-list'),
    path('post/<int:pk>/',           PostDetailView.as_view(), name='post-detail'),

    # (Optional) legacy aliases if كنت مستخدمها قبل كده
    path('posts/new/',               PostCreateView.as_view(), name='post-create-legacy'),
    path('posts/<int:pk>/edit/',     PostUpdateView.as_view(), name='post-edit-legacy'),
    path('posts/<int:pk>/delete/',   PostDeleteView.as_view(), name='post-delete-legacy'),
]
from django.urls import path
from . import views

urlpatterns = [
    # باقي الـ urls هنا...
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
]
from . import views

urlpatterns = [
    # باقي الروابط ...
    path('comment/<int:pk>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
]
from django.urls import path
from . import views

urlpatterns = [
    # Existing post URLs
    path('', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs
    path('post/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment-edit'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
]
from django.urls import path
from . import views

urlpatterns = [
    # existing URLs for posts
    path('', views.post_list, name='post_list'),', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),

    # comment URLs
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    
    # مسار التاجات
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts-by-tag'),
]