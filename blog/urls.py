from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Home and search
    path('', views.HomeView.as_view(), name='home'),
    path('search/', views.SearchView.as_view(), name='search'),
    
    # Post management
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/comment/', views.add_comment, name='add_comment'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    
    # Category and tag filtering
    path('category/<slug:slug>/', views.CategoryPostsView.as_view(), name='category_posts'),
    path('tag/<slug:slug>/', views.TagPostsView.as_view(), name='tag_posts'),
    
    # Author dashboard
    path('dashboard/', views.AuthorDashboardView.as_view(), name='author_dashboard'),
    
    # Comment moderation
    path('comment/<int:pk>/approve/', views.approve_comment, name='approve_comment'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
]
