from rest_framework import routers
from django.urls import path, include
from .views import AuthorViewSet, BookViewSet

router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]