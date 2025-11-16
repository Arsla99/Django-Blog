from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from blog.models import Category, Tag, Post, Comment
from django.utils.text import slugify
import random

User = get_user_model()


class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating sample data...')

        # Create users
        self.stdout.write('Creating users...')
        
        # Create admin
        admin, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'role': 'admin',
                'is_staff': True,
                'is_superuser': True,
                'first_name': 'Admin',
                'last_name': 'User'
            }
        )
        if created:
            admin.set_password('admin123')
            admin.save()
            self.stdout.write(self.style.SUCCESS(f'Created admin user: admin / admin123'))

        # Create authors
        authors = []
        author_data = [
            ('john_author', 'john@example.com', 'John', 'Doe'),
            ('jane_author', 'jane@example.com', 'Jane', 'Smith'),
        ]
        
        for username, email, first_name, last_name in author_data:
            author, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'email': email,
                    'role': 'author',
                    'first_name': first_name,
                    'last_name': last_name
                }
            )
            if created:
                author.set_password('author123')
                author.save()
                self.stdout.write(self.style.SUCCESS(f'Created author: {username} / author123'))
            authors.append(author)

        # Create readers
        readers = []
        reader_data = [
            ('reader1', 'reader1@example.com', 'Alice', 'Johnson'),
            ('reader2', 'reader2@example.com', 'Bob', 'Williams'),
        ]
        
        for username, email, first_name, last_name in reader_data:
            reader, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'email': email,
                    'role': 'reader',
                    'first_name': first_name,
                    'last_name': last_name
                }
            )
            if created:
                reader.set_password('reader123')
                reader.save()
                self.stdout.write(self.style.SUCCESS(f'Created reader: {username} / reader123'))
            readers.append(reader)

        # Create categories
        self.stdout.write('Creating categories...')
        categories_data = [
            ('Technology', 'Explore the latest in tech and innovation'),
            ('Travel', 'Discover amazing destinations around the world'),
            ('Food', 'Delicious recipes and culinary adventures'),
            ('Lifestyle', 'Tips for living your best life'),
            ('Business', 'Business insights and entrepreneurship'),
        ]
        
        categories = []
        for name, description in categories_data:
            category, created = Category.objects.get_or_create(
                slug=slugify(name),
                defaults={'name': name, 'description': description}
            )
            categories.append(category)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {name}'))

        # Create tags
        self.stdout.write('Creating tags...')
        tags_data = [
            'Python', 'Django', 'Web Development', 'AI', 'Machine Learning',
            'Travel Tips', 'Photography', 'Cooking', 'Health', 'Fitness',
            'Productivity', 'Startup', 'Marketing', 'Design', 'Tutorial'
        ]
        
        tags = []
        for name in tags_data:
            tag, created = Tag.objects.get_or_create(
                slug=slugify(name),
                defaults={'name': name}
            )
            tags.append(tag)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created tag: {name}'))

        # Create posts
        self.stdout.write('Creating posts...')
        posts_data = [
            {
                'title': 'Getting Started with Django: A Comprehensive Guide',
                'content': '''<h2>Introduction to Django</h2>
                <p>Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.</p>
                <h3>Why Choose Django?</h3>
                <ul>
                    <li>Fast development</li>
                    <li>Security features built-in</li>
                    <li>Scalable architecture</li>
                    <li>Excellent documentation</li>
                </ul>
                <p>In this guide, we'll explore the fundamentals of Django development...</p>''',
                'category': 'Technology',
                'tags': ['Python', 'Django', 'Web Development', 'Tutorial'],
                'status': 'published'
            },
            {
                'title': 'Top 10 Travel Destinations for 2025',
                'content': '''<h2>Discover Amazing Places</h2>
                <p>As we move into 2025, here are the top destinations you should consider visiting.</p>
                <h3>1. Bali, Indonesia</h3>
                <p>Known for its beautiful beaches and rich culture...</p>
                <h3>2. Iceland</h3>
                <p>Experience the Northern Lights and stunning landscapes...</p>''',
                'category': 'Travel',
                'tags': ['Travel Tips', 'Photography'],
                'status': 'published'
            },
            {
                'title': 'Mastering AI and Machine Learning in 2025',
                'content': '''<h2>The Future of AI</h2>
                <p>Artificial Intelligence and Machine Learning are transforming industries worldwide.</p>
                <h3>Key Trends</h3>
                <ul>
                    <li>Natural Language Processing</li>
                    <li>Computer Vision</li>
                    <li>Reinforcement Learning</li>
                </ul>''',
                'category': 'Technology',
                'tags': ['AI', 'Machine Learning', 'Python'],
                'status': 'published'
            },
            {
                'title': '5 Delicious Pasta Recipes You Must Try',
                'content': '''<h2>Italian Cooking at Home</h2>
                <p>Learn to make authentic Italian pasta dishes in your own kitchen.</p>
                <h3>Recipe 1: Classic Carbonara</h3>
                <p>Ingredients: Pasta, eggs, pancetta, cheese...</p>''',
                'category': 'Food',
                'tags': ['Cooking', 'Food'],
                'status': 'published'
            },
            {
                'title': 'Building a Successful Startup: Lessons Learned',
                'content': '''<h2>Entrepreneurship Journey</h2>
                <p>Starting a business is challenging but rewarding. Here's what I learned.</p>
                <h3>Key Takeaways</h3>
                <ol>
                    <li>Validate your idea early</li>
                    <li>Build a strong team</li>
                    <li>Focus on customer feedback</li>
                </ol>''',
                'category': 'Business',
                'tags': ['Startup', 'Business', 'Productivity'],
                'status': 'published'
            },
            {
                'title': 'Web Design Trends for Modern Applications',
                'content': '''<h2>Stay Ahead with Design</h2>
                <p>The world of web design is constantly evolving. Here are the latest trends.</p>
                <h3>Minimalism</h3>
                <p>Less is more - clean, simple designs are in...</p>''',
                'category': 'Technology',
                'tags': ['Design', 'Web Development'],
                'status': 'published'
            },
            {
                'title': 'Draft: Upcoming Technology Predictions',
                'content': '''<h2>Future Tech</h2>
                <p>This is a draft post about upcoming technology trends...</p>''',
                'category': 'Technology',
                'tags': ['AI', 'Technology'],
                'status': 'draft'
            },
        ]

        for post_data in posts_data:
            category = Category.objects.get(name=post_data['category'])
            post_tags = []
            for tag_name in post_data['tags']:
                try:
                    tag = Tag.objects.get(name=tag_name)
                    post_tags.append(tag)
                except Tag.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f'Tag not found: {tag_name}'))
            
            post, created = Post.objects.get_or_create(
                slug=slugify(post_data['title']),
                defaults={
                    'title': post_data['title'],
                    'content': post_data['content'],
                    'author': random.choice(authors),
                    'category': category,
                    'status': post_data['status'],
                    'views': random.randint(10, 500)
                }
            )
            
            if created:
                post.tags.set(post_tags)
                self.stdout.write(self.style.SUCCESS(f'Created post: {post.title}'))

        # Create comments
        self.stdout.write('Creating comments...')
        published_posts = Post.objects.filter(status='published')
        
        comments_data = [
            "Great article! Very informative.",
            "Thanks for sharing this. I learned a lot!",
            "This is exactly what I was looking for.",
            "Interesting perspective. I have a different view though.",
            "Awesome content! Keep it up!",
            "Can you elaborate more on this topic?",
            "Well written and easy to understand.",
        ]

        for post in published_posts[:5]:  # Add comments to first 5 published posts
            for _ in range(random.randint(2, 4)):
                user = random.choice(readers + authors)
                content = random.choice(comments_data)
                
                Comment.objects.create(
                    post=post,
                    user=user,
                    content=content,
                    approved=random.choice([True, True, False])  # 2/3 approved
                )
        
        self.stdout.write(self.style.SUCCESS('Created comments'))

        self.stdout.write(self.style.SUCCESS('\n=== Sample Data Created Successfully! ==='))
        self.stdout.write(self.style.SUCCESS('\nLogin Credentials:'))
        self.stdout.write(self.style.SUCCESS('Admin: admin / admin123'))
        self.stdout.write(self.style.SUCCESS('Authors: john_author / author123, jane_author / author123'))
        self.stdout.write(self.style.SUCCESS('Readers: reader1 / reader123, reader2 / reader123'))
