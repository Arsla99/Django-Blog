from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post, Category, Tag, Comment
from .forms import PostForm, CommentForm, SearchForm


class HomeView(ListView):
    """Home page with list of published posts"""
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 9
    
    def get_queryset(self):
        return Post.objects.filter(status='published').select_related('author', 'category').prefetch_related('tags')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm()
        context['categories'] = Category.objects.annotate(post_count=Count('posts')).filter(post_count__gt=0)
        context['tags'] = Tag.objects.annotate(post_count=Count('posts')).filter(post_count__gt=0)
        return context


class PostDetailView(DetailView):
    """Post detail view with comments"""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated and self.request.user.is_author():
            return qs
        return qs.filter(status='published')
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # Increment view count
        obj.views += 1
        obj.save(update_fields=['views'])
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(approved=True).select_related('user')
        context['comment_form'] = CommentForm()
        return context


@login_required
def add_comment(request, slug):
    """Add a comment to a post"""
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            
            if comment.approved:
                messages.success(request, 'Your comment has been added.')
            else:
                messages.info(request, 'Your comment is pending approval.')
            
            return redirect('blog:post_detail', slug=slug)
    
    return redirect('blog:post_detail', slug=slug)


class CategoryPostsView(ListView):
    """Posts filtered by category"""
    model = Post
    template_name = 'blog/category_posts.html'
    context_object_name = 'posts'
    paginate_by = 9
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(category=self.category, status='published').select_related('author', 'category')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class TagPostsView(ListView):
    """Posts filtered by tag"""
    model = Post
    template_name = 'blog/tag_posts.html'
    context_object_name = 'posts'
    paginate_by = 9
    
    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return Post.objects.filter(tags=self.tag, status='published').select_related('author', 'category')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context


class SearchView(ListView):
    """Search posts by title or content"""
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'posts'
    paginate_by = 9
    
    def get_queryset(self):
        query = self.request.GET.get('query', '')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query),
                status='published'
            ).select_related('author', 'category')
        return Post.objects.none()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('query', '')
        context['search_form'] = SearchForm(initial={'query': context['query']})
        return context


class AuthorDashboardView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """Dashboard for authors to manage their posts"""
    model = Post
    template_name = 'blog/author_dashboard.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def test_func(self):
        return self.request.user.is_author()
    
    def get_queryset(self):
        if self.request.user.is_admin():
            return Post.objects.all().select_related('author', 'category')
        return Post.objects.filter(author=self.request.user).select_related('category')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_admin():
            context['pending_comments'] = Comment.objects.filter(approved=False).select_related('user', 'post')[:10]
        else:
            context['pending_comments'] = Comment.objects.filter(
                post__author=self.request.user,
                approved=False
            ).select_related('user', 'post')[:10]
        return context


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """Create a new post"""
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:author_dashboard')
    
    def test_func(self):
        return self.request.user.is_author()
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Post created successfully!')
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Update an existing post"""
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:author_dashboard')
    
    def test_func(self):
        post = self.get_object()
        return self.request.user.is_admin() or post.author == self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Post updated successfully!')
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a post"""
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:author_dashboard')
    
    def test_func(self):
        post = self.get_object()
        return self.request.user.is_admin() or post.author == self.request.user
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Post deleted successfully!')
        return super().delete(request, *args, **kwargs)


@login_required
def approve_comment(request, pk):
    """Approve a comment"""
    comment = get_object_or_404(Comment, pk=pk)
    
    # Check permissions
    if not (request.user.is_admin() or comment.post.author == request.user):
        messages.error(request, 'You do not have permission to approve this comment.')
        return redirect('blog:home')
    
    comment.approved = True
    comment.save()
    messages.success(request, 'Comment approved successfully!')
    
    return redirect('blog:author_dashboard')


@login_required
def delete_comment(request, pk):
    """Delete a comment"""
    comment = get_object_or_404(Comment, pk=pk)
    
    # Check permissions
    if not (request.user.is_admin() or comment.post.author == request.user):
        messages.error(request, 'You do not have permission to delete this comment.')
        return redirect('blog:home')
    
    comment.delete()
    messages.success(request, 'Comment deleted successfully!')
    
    return redirect('blog:author_dashboard')
