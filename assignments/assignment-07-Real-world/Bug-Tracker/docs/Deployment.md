# Deployment

## Production Stack

- Ubuntu Server
- Python
- Django
- Gunicorn
- Nginx
- PostgreSQL
- Redis
- Celery

---

## Environment Variables

- SECRET_KEY
- DEBUG
- ALLOWED_HOSTS
- DATABASE_URL
- EMAIL_HOST
- EMAIL_PORT
- EMAIL_HOST_USER
- EMAIL_HOST_PASSWORD
- EMAIL_USE_TLS

---

## Deployment Checklist

- Collect static files
- Apply migrations
- Configure Gunicorn
- Configure Nginx
- Configure Redis
- Configure Celery
- Configure environment variables
- Enable HTTPS
- Restart services

---

## Security Checklist

- DEBUG = False
- Strong SECRET_KEY
- HTTPS enabled
- Secure cookies
- CSRF protection enabled
- XSS protection enabled
- SQL Injection protection
- Regular backups

---

## Monitoring

- Check application logs
- Check Gunicorn logs
- Check Nginx logs
- Monitor database
- Monitor Celery workers