from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # لو عندك خصائص إضافية ممكن تضيفها هنا
    # مثلا:
    # list_display = ['username', 'email', 'role', 'is_staff']
    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ('role',)}),
    # )

admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
