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
from .forms import CustomUserCreationForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# عرض كل البوستات
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # اسم التمبليت
    context_object_name = 'posts'
    ordering = ['-created_at']  # أحدث بوست الأول

# عرض تفاصيل بوست واحد
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# إنشاء بوست جديد
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # يربط البوست باليوزر الحالي
        return super().form_valid(form)

# تعديل بوست
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# حذف بوست
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author