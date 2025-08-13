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