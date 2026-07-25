# API

## Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /register/ | Register a new user |
| POST | /login/ | Login |
| POST | /logout/ | Logout |
| POST | /password-reset/ | Reset password |

---

## Projects

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /projects/ | List projects |
| GET | /projects/<id>/ | Project details |
| POST | /projects/create/ | Create project |
| POST | /projects/<id>/edit/ | Edit project |
| POST | /projects/<id>/delete/ | Delete project |

---

## Tickets

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /tickets/ | List tickets |
| GET | /tickets/<id>/ | Ticket details |
| POST | /tickets/create/ | Create ticket |
| POST | /tickets/<id>/edit/ | Edit ticket |
| POST | /tickets/<id>/delete/ | Delete ticket |
| POST | /tickets/<id>/assign/ | Assign developer |
| POST | /tickets/<id>/status/ | Update status |

---

## Comments

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /tickets/<id>/comments/create/ | Add comment |
| POST | /comments/<id>/edit/ | Edit comment |
| POST | /comments/<id>/delete/ | Delete comment |

---

## Notifications

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /notifications/ | List notifications |
| POST | /notifications/<id>/read/ | Mark as read |