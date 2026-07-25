# Bug Tracker

A production-ready bug tracking system built with Django.

The project is designed to demonstrate backend engineering, clean architecture, security best practices, testing, performance optimization, and deployment.

## Features

- User authentication
- Project management
- Bug tracking
- Ticket assignment
- Comments
- Email notifications
- Background tasks with Celery
- Query optimization
- Caching
- Security best practices
- Automated testing

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

## Documentation

Project documentation is available inside the `docs/` directory.

- Bug Tracker Plan
- Architecture
- Database Design
- API
- Deployment
- Release Checklist
- Changelog

## Installation

```bash
git clone <repository-url>

cd Bug-Tracker

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

## Testing

Run all tests.

```bash
python manage.py test
```

## Future Improvements

- REST API
- Docker support
- CI/CD
- WebSocket notifications
- File attachments
- Activity log

## License

This project is created for learning, portfolio, and educational purposes.