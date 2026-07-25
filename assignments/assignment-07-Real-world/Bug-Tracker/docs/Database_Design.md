# Database Design

## User

Django built-in User model.

Relationships:

- Owns many projects.
- Can be assigned many tickets.
- Can create many tickets.
- Can write many comments.

---

## Project

Fields:

- Owner
- Name
- Description
- Created At
- Updated At

Relationships:

- One project has many members.
- One project has many tickets.

---

## Ticket

Fields:

- Project
- Reporter
- Assigned Developer
- Title
- Description
- Status
- Priority
- Deadline
- Created At
- Updated At

Relationships:

- One ticket belongs to one project.
- One ticket has many comments.

---

## Comment

Fields:

- Ticket
- Author
- Content
- Created At

Relationships:

- One comment belongs to one ticket.
- One comment belongs to one user.

---

## Notification

Fields:

- User
- Ticket
- Message
- Is Read
- Created At

Relationships:

- One user has many notifications.
- One notification may reference one ticket.

---

## Relationships

User
│
├── Owns → Projects
├── Reports → Tickets
├── Assigned → Tickets
└── Writes → Comments

Project
│
├── Members
└── Tickets

Ticket
│
└── Comments