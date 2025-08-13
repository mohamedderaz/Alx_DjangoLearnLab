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
    
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import CommentForm

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # لسه مخلصناش الحفظ
            comment.post = post               # نربط التعليق بالمقالة
            comment.author = request.user     # نربط التعليق بالمستخدم الحالي
            comment.save()
            return redirect('post_detail', pk=post.pk)  # بعد الحفظ نرجع لصفحة المقالة
    else:
        form = CommentForm()

    return render(request, 'blog/add_comment.html', {'form': form, 'post': post})
from .models import Post, Comment
from .forms import CommentForm

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-created_at')  # نعرض التعليقات الأحدث أول

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('post_detail', pk=post.pk)
        else:
            return redirect('login')
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })
@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.author != request.user and not request.user.is_superuser:
        return redirect('post_detail', pk=comment.post.pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/edit_comment.html', {'form': form})
@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.author != request.user and not request.user.is_superuser:
        return redirect('post_detail', pk=comment.post.pk)

    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', pk=comment.post.pk)

    return render(request, 'blog/delete_comment.html', {'comment': comment})