from django.contrib import admin
from .models import Post, Category, Tag, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin for Category model"""
    list_display = ['name', 'slug', 'created_at']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin for Tag model"""
    list_display = ['name', 'slug', 'created_at']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


class CommentInline(admin.TabularInline):
    """Inline admin for comments in post admin"""
    model = Comment
    extra = 0
    readonly_fields = ['user', 'created_at']
    fields = ['user', 'content', 'approved', 'created_at']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin for Post model"""
    list_display = ['title', 'author', 'category', 'status', 'views', 'created_at', 'published_at']
    list_filter = ['status', 'category', 'tags', 'created_at', 'published_at']
    search_fields = ['title', 'content', 'author__username']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['tags']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    inlines = [CommentInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'author', 'status')
        }),
        ('Content', {
            'fields': ('content', 'excerpt', 'featured_image')
        }),
        ('Categorization', {
            'fields': ('category', 'tags')
        }),
        ('Meta Information', {
            'fields': ('views', 'published_at'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        """Auto-set author to current user if creating new post"""
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin for Comment model"""
    list_display = ['user', 'post', 'approved', 'created_at']
    list_filter = ['approved', 'created_at']
    search_fields = ['user__username', 'post__title', 'content']
    actions = ['approve_comments', 'disapprove_comments']
    ordering = ['-created_at']
    
    def approve_comments(self, request, queryset):
        """Bulk approve comments"""
        queryset.update(approved=True)
        self.message_user(request, f'{queryset.count()} comments approved.')
    approve_comments.short_description = 'Approve selected comments'
    
    def disapprove_comments(self, request, queryset):
        """Bulk disapprove comments"""
        queryset.update(approved=False)
        self.message_user(request, f'{queryset.count()} comments disapproved.')
    disapprove_comments.short_description = 'Disapprove selected comments'
