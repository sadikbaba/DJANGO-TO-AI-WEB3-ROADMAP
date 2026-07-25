# 🐞 Bug Tracker

> A production-ready Bug Tracking System built with Django.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-5.x-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Redis](https://img.shields.io/badge/Redis-Cache-red)
![Celery](https://img.shields.io/badge/Celery-Background%20Tasks-brightgreen)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

---

## Overview

Bug Tracker is a production-ready web application for managing software projects and tracking bugs.

The project is designed to demonstrate backend engineering, clean architecture, security, testing, performance optimization, and deployment using Django.

---

## Learning Goals

This project demonstrates practical experience with:

- Clean Architecture
- Django Best Practices
- Database Design
- Query Optimization
- Authentication
- Authorization
- Security Best Practices
- Automated Testing
- Caching
- Background Tasks with Celery
- Production Deployment

---

## Features

- User authentication
- Project management
- Ticket management
- Ticket assignment
- Comments
- Email notifications
- Background tasks with Celery
- Redis caching
- Query optimization
- Security best practices
- Automated testing

---

## Tech Stack

- Python
- Django
- PostgreSQL
- Redis
- Celery
- Gunicorn
- Nginx
- HTML
- CSS

---

## Project Structure

```text
apps/
    accounts/
    projects/
    tickets/
    comments/
    notifications/

config/

docs/
```

---

## Documentation

Detailed documentation is available in the `docs/` directory.

- Bug Tracker Plan
- Architecture
- Database Design
- API
- Deployment
- Release Checklist
- Changelog

---

## Installation

```bash
git clone https://github.com/sadikbaba/DJANGO-TO-AI-WEB3-ROADMAP.git

cd DJANGO-TO-AI-WEB3-ROADMAP/Bug-Tracker

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

---

## Testing

Run all tests.

```bash
python manage.py test
```

---

## Development Roadmap

- [ ] Accounts
- [ ] Projects
- [ ] Tickets
- [ ] Comments
- [ ] Notifications
- [ ] Caching
- [ ] Testing
- [ ] Deployment

---

## Future Improvements

- Django REST Framework API
- Docker support
- CI/CD
- WebSocket notifications
- File attachments
- Activity log

---

## License

This project is built for learning, portfolio, and educational purposes.