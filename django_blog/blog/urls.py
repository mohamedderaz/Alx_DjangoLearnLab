from django.urls import path
from .views import (
    BlogLoginView, BlogLogoutView, register, profile
)

urlpatterns = [
    path('login',  BlogLoginView.as_view(), name='login'),      # /login
    path('logout', BlogLogoutView.as_view(), name='logout'),    # /logout
    path('register', register, name='register'),                # /register
    path('profile', profile, name='profile'),                  # /profile
]