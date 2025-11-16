from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """Form for creating and editing blog posts"""
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'excerpt', 'featured_image', 'category', 'tags', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter post title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Auto-generated from title'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Brief description...'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.CheckboxSelectMultiple(),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slug'].required = False


class CommentForm(forms.ModelForm):
    """Form for adding comments to posts"""
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your comment here...'
            })
        }
        labels = {
            'content': 'Your Comment'
        }


class SearchForm(forms.Form):
    """Form for searching posts"""
    query = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search posts...'
        })
    )
