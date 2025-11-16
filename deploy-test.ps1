# Railway Deployment Quick Start

Write-Host "Django Blog - Railway Deployment Setup" -ForegroundColor Cyan
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host ""

# Check if virtual environment is activated
if (-not $env:VIRTUAL_ENV) {
    Write-Host "Warning: No virtual environment detected!" -ForegroundColor Yellow
    Write-Host "It's recommended to use a virtual environment." -ForegroundColor Yellow
    Write-Host ""
    $continue = Read-Host "Continue anyway? (y/n)"
    if ($continue -ne "y") {
        exit
    }
}

# Step 1: Install production dependencies
Write-Host "Step 1: Installing production dependencies..." -ForegroundColor Green
pip install -r requirements.txt

if ($LASTEXITCODE -ne 0) {
    Write-Host "Error installing dependencies!" -ForegroundColor Red
    exit 1
}

# Step 2: Collect static files
Write-Host ""
Write-Host "Step 2: Collecting static files..." -ForegroundColor Green
python manage.py collectstatic --noinput

if ($LASTEXITCODE -ne 0) {
    Write-Host "Error collecting static files!" -ForegroundColor Red
    exit 1
}

# Step 3: Test gunicorn locally
Write-Host ""
Write-Host "Step 3: Testing Gunicorn server..." -ForegroundColor Green
Write-Host "Starting Gunicorn on http://127.0.0.1:8000" -ForegroundColor Cyan
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

gunicorn advanced_blog.wsgi --bind 127.0.0.1:8000 --log-level debug

Write-Host ""
Write-Host "Gunicorn test complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps for Railway deployment:" -ForegroundColor Cyan
Write-Host "1. Commit all changes: git add . && git commit -m 'Add Railway deployment'" -ForegroundColor White
Write-Host "2. Push to GitHub: git push origin main" -ForegroundColor White
Write-Host "3. Deploy on Railway: https://railway.app" -ForegroundColor White
Write-Host "4. Add PostgreSQL database in Railway" -ForegroundColor White
Write-Host "5. Set environment variables (SECRET_KEY, DEBUG, ALLOWED_HOSTS)" -ForegroundColor White
Write-Host "6. Create superuser: python manage.py createsuperuser" -ForegroundColor White
Write-Host ""
Write-Host "See RAILWAY_DEPLOYMENT.md for detailed instructions!" -ForegroundColor Cyan
