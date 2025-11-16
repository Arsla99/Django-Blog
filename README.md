# Advanced Blog Platform

A full-featured blog platform built with Django that includes advanced features such as user authentication, role-based permissions, comments, categories, tags, and search functionality.

![Django](https://img.shields.io/badge/Django-5.2.8-green.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)

## 🌟 Features

### User Management
- **Custom User Model** with role-based permissions (Admin, Author, Reader)
- User registration and authentication
- User profile management with bio and profile image
- Activity tracking middleware

### Blog Features
- **Post Management**: Create, read, update, and delete posts
- **Rich Text Editor**: CKEditor integration for content creation
- **Post Status**: Draft and Published states
- **Featured Images**: Upload and display images for posts
- **Categories & Tags**: Organize posts with categories and multiple tags
- **SEO-Friendly URLs**: Slug-based URLs for posts, categories, and tags
- **View Counter**: Track post views

### Comment System
- User comments on posts
- Comment moderation (approve/delete)
- Auto-approval for authors and admins
- Comment filtering by approval status

### Search & Filter
- Full-text search across post titles and content
- Filter posts by category
- Filter posts by tags
- Pagination for all list views

### Author Dashboard
- Manage all posts (create, edit, delete)
- View post statistics (views, comments)
- Moderate pending comments
- Draft and publish management

### Admin Panel
- Customized Django admin interface
- Bulk actions for comment approval
- Enhanced filtering and search
- Inline comment management

## 🛠️ Technology Stack

- **Backend**: Django 5.2.8
- **Database**: SQLite (development) / PostgreSQL (production recommended)
- **Frontend**: Bootstrap 5.3, Bootstrap Icons
- **Rich Text Editor**: CKEditor 4
- **Image Processing**: Pillow
- **Configuration**: python-decouple

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd advanced_blog
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables (Optional)

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 7. Create Initial Data (Optional)

Create some categories and tags in the Django admin panel or via the Django shell:

```bash
python manage.py shell
```

```python
from blog.models import Category, Tag

# Create categories
Category.objects.create(name="Technology", slug="technology")
Category.objects.create(name="Travel", slug="travel")
Category.objects.create(name="Food", slug="food")

# Create tags
Tag.objects.create(name="Python", slug="python")
Tag.objects.create(name="Django", slug="django")
Tag.objects.create(name="Web Development", slug="web-development")
```

### 8. Collect Static Files (For Production)

```bash
python manage.py collectstatic
```

### 9. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## 📱 Usage

### User Roles

1. **Admin**
   - Full access to all features
   - Manage all posts, comments, categories, and tags
   - Access to Django admin panel

2. **Author**
   - Create, edit, and delete own posts
   - View author dashboard
   - Moderate comments on own posts
   - Auto-approved comments

3. **Reader** (Default)
   - View published posts
   - Add comments (require approval)
   - Search and filter posts

### Creating Your First Post

1. Register or login as an Author or Admin
2. Navigate to "Create Post" from the navbar
3. Fill in the post details:
   - Title (required)
   - Content (required)
   - Excerpt (optional, auto-generated from content)
   - Featured Image (optional)
   - Category and Tags
   - Status (Draft or Published)
4. Click "Save Post"

### Managing Comments

1. Go to the Author Dashboard
2. View pending comments
3. Approve or delete comments as needed

## 📁 Project Structure

```
advanced_blog/
├── accounts/                 # User management app
│   ├── migrations/
│   ├── admin.py             # Custom user admin
│   ├── forms.py             # Registration and profile forms
│   ├── middleware.py        # User activity tracking
│   ├── models.py            # Custom user model
│   ├── urls.py              # Account URLs
│   └── views.py             # Auth views
├── blog/                     # Blog functionality app
│   ├── migrations/
│   ├── admin.py             # Post, category, tag, comment admin
│   ├── forms.py             # Post and comment forms
│   ├── models.py            # Post, category, tag, comment models
│   ├── signals.py           # Post publication signals
│   ├── urls.py              # Blog URLs
│   └── views.py             # Blog views
├── advanced_blog/           # Project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   ├── accounts/            # Auth templates
│   └── blog/                # Blog templates
├── static/                  # Static files
│   └── css/
│       └── style.css        # Custom styles
├── media/                   # User uploaded files
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

## 🎨 Database Schema

### CustomUser Model
- Extends Django's AbstractUser
- Fields: username, email, password, role, bio, profile_image, last_activity

### Post Model
- Fields: title, slug, content, excerpt, featured_image, author (FK), category (FK), tags (M2M), status, views, created_at, updated_at, published_at

### Category Model
- Fields: name, slug, description, created_at

### Tag Model
- Fields: name, slug, created_at

### Comment Model
- Fields: post (FK), user (FK), content, approved, created_at, updated_at

## 🔒 Security Features

- CSRF protection on all forms
- Password validation
- User authentication required for sensitive operations
- Role-based access control
- Comment moderation
- XSS protection via Django's auto-escaping

## 🚀 Deployment

### Railway Deployment (Recommended)

**Railway** is the easiest way to deploy this Django application with automatic PostgreSQL provisioning and zero-config deployment.

#### Quick Deploy Steps:

1. **Prepare your repository**:
   ```powershell
   git add .
   git commit -m "Add Railway deployment configuration"
   git push origin main
   ```

2. **Deploy on Railway**:
   - Go to [railway.app](https://railway.app) and sign in
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Railway will automatically detect Django and deploy!

3. **Add PostgreSQL**:
   - In your Railway project, click "New" → "Database" → "Add PostgreSQL"
   - `DATABASE_URL` will be automatically configured

4. **Set Environment Variables**:
   Go to your web service → Variables tab and add:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=your-app.up.railway.app
   ```

5. **Create Superuser**:
   In Railway console, run:
   ```bash
   python manage.py createsuperuser
   ```

6. **(Optional) Add Sample Data**:
   ```bash
   python manage.py populate_data
   ```

**📖 For detailed deployment instructions, see [RAILWAY_DEPLOYMENT.md](RAILWAY_DEPLOYMENT.md)**

#### Local Deployment Test:

Test Railway configuration locally before deploying:

```powershell
.\deploy-test.ps1
```

This will:
- Install production dependencies
- Collect static files
- Start Gunicorn server locally

### Alternative: Heroku Deployment

1. Install Heroku CLI and login:
```bash
heroku login
```

2. Create a new Heroku app:
```bash
heroku create your-app-name
```

3. Add PostgreSQL addon:
```bash
heroku addons:create heroku-postgresql:mini
```

4. Deploy:
```bash
git add .
git commit -m "Prepare for deployment"
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Alternative: PythonAnywhere Deployment

1. Create account on PythonAnywhere
2. Upload project files
3. Create virtual environment
4. Configure WSGI file
5. Set up static files mapping
6. Run migrations

Detailed guides available in the Django documentation.

## 📸 Screenshots

### Home Page
- Displays latest published posts in a grid layout
- Sidebar with categories and tags
- Search functionality in navbar

### Post Detail
- Full post content with rich text formatting
- Comments section
- Author information

### Author Dashboard
- Statistics overview
- Post management table
- Pending comments list

### Admin Panel
- Enhanced Django admin with custom filters
- Bulk actions for comments
- Inline comment management

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is created for educational purposes as part of a Django learning project.

## 👨‍💻 Author

Created as a demonstration of Django best practices and full-stack web development.

## 📞 Support

For issues or questions, please open an issue on the repository.

## 🔄 Updates & Roadmap

### Current Version: 1.0.0

### Planned Features:
- [ ] Email notifications for comments
- [ ] Social media sharing
- [ ] Post bookmarking
- [ ] Advanced analytics dashboard
- [ ] RSS feed
- [ ] API endpoints (REST API)
- [ ] Multi-language support
- [ ] Dark mode toggle
- [ ] Newsletter subscription

## 📚 Learning Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [CKEditor Documentation](https://ckeditor.com/docs/)

---

**Note**: This is a learning project. For production use, ensure proper security measures, use environment variables for sensitive data, and implement proper backup strategies.
