# Architecture

## Project Structure

```
Bug-Tracker/
│
├── apps/
│   ├── accounts/
│   ├── projects/
│   ├── tickets/
│   ├── comments/
│   └── notifications/
│
├── config/
├── docs/
├── manage.py
├── README.md
└── requirements.txt
```

---

## Apps

### accounts

Responsible for:

- Registration
- Login
- Logout
- Password reset
- User profile

---

### projects

Responsible for:

- Project management
- Project members
- Project permissions

---

### tickets

Responsible for:

- Ticket management
- Status updates
- Priority
- Assignment

---

### comments

Responsible for:

- Ticket discussions
- Comment history

---

### notifications

Responsible for:

- Email notifications
- Celery tasks
- Signals

---

## Request Flow

```
Browser

↓

URL

↓

View

↓

Form

↓

Model

↓

Database

↓

Template

↓

Browser
```

---

## Development Rules

- One feature at a time
- One responsibility per app
- Every feature must have tests
- Every feature must be tested in the browser
- Security review before moving to the next feature
- Optimize queries when necessary

---

## Testing Strategy

Every app should contain:

- Model tests
- View tests
- Form tests
- Permission tests

Every completed feature must also be tested manually in the browser.

---

## Performance

Use:

- `select_related()` for ForeignKey and OneToOne relationships.
- `prefetch_related()` for ManyToMany and reverse ForeignKey relationships.
- Caching where repeated database queries occur.

---

## Security

Apply throughout the project:

- Authentication
- Authorization
- CSRF protection
- XSS protection
- SQL Injection prevention