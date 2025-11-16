# Deployment Guide for Advanced Blog Platform

This guide provides detailed instructions for deploying the Advanced Blog Platform to various hosting providers.

## Table of Contents
1. [Pre-Deployment Checklist](#pre-deployment-checklist)
2. [Heroku Deployment](#heroku-deployment)
3. [PythonAnywhere Deployment](#pythonanywhere-deployment)
4. [AWS EC2 Deployment](#aws-ec2-deployment)
5. [Production Settings](#production-settings)

---

## Pre-Deployment Checklist

Before deploying, ensure you have:

- [ ] All code committed to version control (Git)
- [ ] `requirements.txt` up to date
- [ ] Environment variables configured
- [ ] Database migrations tested
- [ ] Static files collected
- [ ] Media files storage configured
- [ ] Secret key secured
- [ ] DEBUG set to False for production

---

## Heroku Deployment

### Prerequisites
- Heroku account
- Heroku CLI installed
- Git repository initialized

### Step 1: Install Additional Dependencies

```bash
pip install gunicorn whitenoise dj-database-url python-decouple psycopg2-binary
pip freeze > requirements.txt
```

### Step 2: Create Procfile

Create a file named `Procfile` in the project root:

```
web: gunicorn advanced_blog.wsgi --log-file -
```

### Step 3: Create runtime.txt

Create `runtime.txt`:

```
python-3.11.9
```

### Step 4: Update settings.py for Heroku

Add to `settings.py`:

```python
import dj_database_url
from decouple import config

# Security settings
SECRET_KEY = config('SECRET_KEY', default='your-secret-key-here')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')

# Database configuration
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', default='sqlite:///db.sqlite3')
    )
}

# WhiteNoise for static files
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    # ... other middleware
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files for production
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'  # If using Cloudinary
```

### Step 5: Deploy to Heroku

```bash
# Login to Heroku
heroku login

# Create new app
heroku create your-app-name

# Add PostgreSQL
heroku addons:create heroku-postgresql:mini

# Set environment variables
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com"

# Deploy
git add .
git commit -m "Prepare for Heroku deployment"
git push heroku main

# Run migrations
heroku run python manage.py migrate

# Create superuser
heroku run python manage.py createsuperuser

# Collect static files
heroku run python manage.py collectstatic --noinput

# Open app
heroku open
```

### Step 6: Configure Media Files (Optional - Using Cloudinary)

```bash
# Install Cloudinary
pip install cloudinary django-cloudinary-storage

# Add to INSTALLED_APPS in settings.py
INSTALLED_APPS = [
    # ...
    'cloudinary_storage',
    'cloudinary',
    # ...
]

# Configure Cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': config('CLOUDINARY_API_KEY'),
    'API_SECRET': config('CLOUDINARY_API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Set environment variables
heroku config:set CLOUDINARY_CLOUD_NAME="your-cloud-name"
heroku config:set CLOUDINARY_API_KEY="your-api-key"
heroku config:set CLOUDINARY_API_SECRET="your-api-secret"
```

---

## PythonAnywhere Deployment

### Step 1: Create PythonAnywhere Account
- Sign up at [PythonAnywhere](https://www.pythonanywhere.com/)
- Choose appropriate plan (free tier available)

### Step 2: Upload Code

**Option A: Using Git**
```bash
# In PythonAnywhere Bash console
git clone https://github.com/yourusername/advanced-blog.git
cd advanced-blog
```

**Option B: Manual Upload**
- Use Files tab to upload project files

### Step 3: Create Virtual Environment

```bash
cd ~/advanced-blog
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Step 4: Configure WSGI

Edit `/var/www/yourusername_pythonanywhere_com_wsgi.py`:

```python
import os
import sys

# Add your project directory to the sys.path
project_home = '/home/yourusername/advanced-blog'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'advanced_blog.settings'

# Activate virtual environment
activate_this = os.path.join(project_home, '.venv/bin/activate_this.py')
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### Step 5: Configure Static and Media Files

In PythonAnywhere Web tab:
- **Static files**
  - URL: `/static/`
  - Directory: `/home/yourusername/advanced-blog/staticfiles/`
  
- **Media files**
  - URL: `/media/`
  - Directory: `/home/yourusername/advanced-blog/media/`

### Step 6: Run Migrations and Collect Static

```bash
cd ~/advanced-blog
source .venv/bin/activate
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

### Step 7: Reload Web App
- Go to Web tab
- Click "Reload" button

---

## AWS EC2 Deployment

### Prerequisites
- AWS account
- EC2 instance (Ubuntu recommended)
- Domain name (optional)

### Step 1: Launch EC2 Instance
1. Choose Ubuntu Server
2. Select instance type (t2.micro for testing)
3. Configure security group:
   - SSH (port 22)
   - HTTP (port 80)
   - HTTPS (port 443)

### Step 2: Connect and Setup

```bash
# Connect to instance
ssh -i your-key.pem ubuntu@your-instance-ip

# Update system
sudo apt update
sudo apt upgrade -y

# Install Python and dependencies
sudo apt install python3-pip python3-venv nginx -y

# Install PostgreSQL
sudo apt install postgresql postgresql-contrib -y
```

### Step 3: Setup Database

```bash
sudo -u postgres psql

# In PostgreSQL prompt
CREATE DATABASE advanced_blog;
CREATE USER bloguser WITH PASSWORD 'your-password';
ALTER ROLE bloguser SET client_encoding TO 'utf8';
ALTER ROLE bloguser SET default_transaction_isolation TO 'read committed';
ALTER ROLE bloguser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE advanced_blog TO bloguser;
\q
```

### Step 4: Deploy Application

```bash
cd /home/ubuntu
git clone your-repo-url advanced-blog
cd advanced-blog

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install gunicorn psycopg2-binary

# Configure environment
cp .env.example .env
nano .env  # Edit with your settings
```

### Step 5: Configure Gunicorn

Create `/etc/systemd/system/gunicorn.service`:

```ini
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/advanced-blog
ExecStart=/home/ubuntu/advanced-blog/.venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/home/ubuntu/advanced-blog/advanced_blog.sock \
          advanced_blog.wsgi:application

[Install]
WantedBy=multi-user.target
```

Start Gunicorn:
```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

### Step 6: Configure Nginx

Create `/etc/nginx/sites-available/advanced-blog`:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /home/ubuntu/advanced-blog;
    }
    
    location /media/ {
        root /home/ubuntu/advanced-blog;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/advanced-blog/advanced_blog.sock;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/advanced-blog /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

### Step 7: SSL Certificate (Optional - Let's Encrypt)

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

---

## Production Settings

### Essential Production Settings

```python
# settings.py

# Security
DEBUG = False
SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']

# HTTPS/SSL
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# HSTS
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# Email configuration (for notifications)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/path/to/django/error.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
```

---

## Post-Deployment Tasks

1. **Test all functionality**
   - User registration and login
   - Post creation and editing
   - Comment submission and approval
   - Search functionality
   - Image uploads

2. **Monitor application**
   - Check error logs
   - Monitor database performance
   - Track user activity

3. **Setup backups**
   - Database backups (daily recommended)
   - Media files backup
   - Code backup

4. **Performance optimization**
   - Enable caching
   - Optimize database queries
   - Use CDN for static files

5. **Security measures**
   - Regular security updates
   - Monitor for vulnerabilities
   - Implement rate limiting
   - Setup firewall rules

---

## Troubleshooting

### Common Issues

**Static files not loading**
```bash
python manage.py collectstatic --noinput
# Check STATIC_ROOT and STATIC_URL settings
```

**Database connection errors**
```bash
# Verify DATABASE_URL or database credentials
# Check if database service is running
```

**Permission errors**
```bash
# Ensure proper file permissions
sudo chown -R www-data:www-data /path/to/project
sudo chmod -R 755 /path/to/project
```

---

## Monitoring and Maintenance

### Recommended Tools
- **Sentry** - Error tracking
- **New Relic** - Performance monitoring
- **Cloudflare** - CDN and DDoS protection
- **Uptime Robot** - Uptime monitoring

---

## Support

For deployment issues, refer to:
- [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)
- [Heroku Python Support](https://devcenter.heroku.com/articles/python-support)
- [PythonAnywhere Help](https://help.pythonanywhere.com/)

---

**Last Updated**: November 2025
