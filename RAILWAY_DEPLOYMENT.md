# Railway Deployment Guide

This guide will walk you through deploying your Django blog application to Railway.

## Prerequisites

- A Railway account (sign up at https://railway.app)
- Git installed on your local machine
- Your code pushed to a Git repository (GitHub, GitLab, or Bitbucket)

## Deployment Files Overview

The following files have been configured for Railway deployment:

1. **Procfile** - Tells Railway how to start the application
2. **runtime.txt** - Specifies Python version (3.11.9)
3. **railway.json** - Railway-specific configuration
4. **requirements.txt** - Updated with production dependencies
5. **settings.py** - Configured for environment variables

## Step-by-Step Deployment

### 1. Prepare Your Code

First, ensure all deployment files are committed to your Git repository:

```bash
git add .
git commit -m "Add Railway deployment configuration"
git push origin main
```

### 2. Create a Railway Project

1. Go to https://railway.app and sign in
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"** (or your Git provider)
4. Choose your repository from the list
5. Railway will automatically detect it's a Django app

### 3. Add PostgreSQL Database

1. In your Railway project, click **"New"**
2. Select **"Database"**
3. Choose **"Add PostgreSQL"**
4. Railway will automatically create a `DATABASE_URL` environment variable

### 4. Configure Environment Variables

Click on your web service, then go to **"Variables"** tab and add:

```
SECRET_KEY=your-secret-key-here-make-it-long-and-random
DEBUG=False
ALLOWED_HOSTS=your-project-name.up.railway.app
```

**Generate a secure SECRET_KEY:**
```python
# Run this in Python to generate a secure key
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 5. Deploy

Railway will automatically deploy your application. The `railway.json` configuration will:
- Run database migrations
- Collect static files
- Start the Gunicorn server

### 6. Create Superuser

After deployment, you need to create an admin user:

1. Go to your Railway project
2. Click on your web service
3. Go to the **"Deployments"** tab
4. Click on the latest deployment
5. Open the **"View Logs"** section
6. Click the **"•••"** menu and select **"Run Command"**
7. Run: `python manage.py createsuperuser`
8. Follow the prompts to create your admin account

### 7. (Optional) Populate Sample Data

To add sample data to your deployed site:

1. In the Railway console (same as step 6)
2. Run: `python manage.py populate_data`

## Post-Deployment Checklist

- [ ] Application is accessible at your Railway URL
- [ ] Admin panel works at `/admin/`
- [ ] Static files (CSS, JS, images) are loading correctly
- [ ] User registration and login work
- [ ] Post creation and editing work
- [ ] Comments system works
- [ ] Search functionality works
- [ ] Images upload correctly

## Troubleshooting

### Static Files Not Loading

If static files aren't loading:
1. Check that WhiteNoise is in `requirements.txt`
2. Verify `STORAGES` configuration in `settings.py`
3. Check Railway logs for `collectstatic` errors

### Database Connection Issues

If you see database connection errors:
1. Ensure PostgreSQL database is created in Railway
2. Verify `DATABASE_URL` is automatically set
3. Check that migrations ran successfully in logs

### Application Crashes

If the app crashes on startup:
1. Check Railway logs for detailed error messages
2. Verify all environment variables are set correctly
3. Ensure `ALLOWED_HOSTS` includes your Railway domain
4. Check that all dependencies in `requirements.txt` are correct

### "DisallowedHost" Error

If you see this error:
1. Update `ALLOWED_HOSTS` environment variable
2. Include your Railway domain: `your-app.up.railway.app`
3. Redeploy the application

## Updating Your Deployment

When you make changes to your code:

```bash
git add .
git commit -m "Your commit message"
git push origin main
```

Railway will automatically detect the changes and redeploy.

## Custom Domain (Optional)

To use your own domain:

1. Go to your Railway project
2. Click on your web service
3. Go to **"Settings"** tab
4. Scroll to **"Domains"** section
5. Click **"Add Domain"**
6. Follow the instructions to configure your DNS

## Environment Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | Random 50-char string |
| `DEBUG` | Debug mode (should be False in production) | False |
| `ALLOWED_HOSTS` | Allowed domains | your-app.up.railway.app |
| `DATABASE_URL` | PostgreSQL connection (auto-set by Railway) | postgresql://... |

## Monitoring

Railway provides:
- **Logs**: Real-time application logs
- **Metrics**: CPU, memory, and network usage
- **Health Checks**: Automatic monitoring

Access these from your Railway dashboard.

## Cost Considerations

- Railway offers a free trial with $5 credit
- Check current pricing at https://railway.app/pricing
- Monitor your usage in the Railway dashboard

## Support

If you encounter issues:
1. Check Railway logs for error messages
2. Review this deployment guide
3. Consult Railway documentation: https://docs.railway.app
4. Railway Discord community: https://discord.gg/railway

## Next Steps

After successful deployment:
1. Test all features thoroughly
2. Create initial content (categories, tags, posts)
3. Invite users to test the platform
4. Monitor performance and logs
5. Set up regular backups (Railway provides automatic backups for Pro plan)

## Security Recommendations

1. **Never commit `.env` files** - They're in `.gitignore`
2. **Use strong SECRET_KEY** - Generate with Django's utility
3. **Keep DEBUG=False** in production
4. **Regularly update dependencies** - Check for security updates
5. **Use HTTPS only** - Railway provides this automatically
6. **Regular backups** - Export database periodically

---

**Congratulations!** Your Django blog is now live on Railway! 🚀
