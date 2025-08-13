from django.urls import path
from .views import (
    BlogLoginView, BlogLogoutView, register, profile
)

urlpatterns = [
    path('login/',  BlogLoginView.as_view(), name='login'),      
    path('logout/', BlogLogoutView.as_view(), name='logout'),    
    path('register/', register, name='register'),                
    path('profile/', profile, name='profile'),                  
]
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]