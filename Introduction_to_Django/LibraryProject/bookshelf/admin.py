from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')   # الأعمدة اللي هتظهر في القائمة
    search_fields = ('title', 'author')                      # إمكانيات البحث
    list_filter = ('publication_year',)                      # فلاتر جانبية

# Register your models here.
