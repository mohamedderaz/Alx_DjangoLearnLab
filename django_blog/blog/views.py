from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login
from .forms import RegisterForm, ProfileForm

# تسجيل الدخول باستخدام الـ built-in view
class BlogLoginView(LoginView):
    template_name = "blog/auth/login.html"

# الخروج باستخدام الـ built-in view
class BlogLogoutView(LogoutView):
    next_page = reverse_lazy('login')

# تسجيل مستخدم جديد
def register(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully. You can log in now.")
            # تقدر تعمل login مباشر لو حابب:
            # login(request, user)
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, "blog/auth/register.html", {"form": form})

# صفحة البروفايل مع التعديل
@login_required
def profile(request):
    profile = request.user.profile  # اتأكد إن سيجنال الإنشاء شغال
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        # تحديث الإيميل من نموذج بسيط في الصفحة
        email = request.POST.get("email", "").strip()
        if form.is_valid():
            form.save()
            if email and email.lower() != request.user.email.lower():
                request.user.email = email
                request.user.save()
            messages.success(request, "Profile updated.")
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, "blog/auth/profile.html", {"form": form})

# Create your views here.
