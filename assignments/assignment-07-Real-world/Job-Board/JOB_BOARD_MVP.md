# Job Board MVP Planning

## 1. Product Goal

The core purpose of this Job Board is to connect:

* Job Seekers
* Employers
* Companies
* Jobs
* Applications

The core business loop is:

```text
Employer
    ↓
Creates Company
    ↓
Publishes Job
    ↓
Job Seeker finds Job
    ↓
Job Seeker applies
    ↓
Employer reviews Application
    ↓
Accepts / Declines
```

---

# 2. User Accounts

Every person has one account.

```text
User
├── Job Seeker capabilities
└── Employer capabilities
```

A user can initially register as a Job Seeker or Employer, but this should not permanently restrict what they can do.

A Job Seeker can later become an Employer.

A user can potentially have both capabilities using the same account.

---

# 3. Registration

Registration should collect only necessary information:

* Username
* Email
* Password
* Full name
* Initial intention:

  * Job Seeker
  * Employer

The initial choice should not permanently lock the user's account.

Example:

```text
User registers
      ↓
Chooses Job Seeker
      ↓
Uses the platform
      ↓
Later clicks "Become an Employer"
      ↓
Completes employer onboarding
```

---

# 4. Job Seeker

A Job Seeker can:

* Browse jobs
* Search jobs
* Filter jobs
* View job details
* Apply for jobs
* View submitted applications
* Track application status

## Job Seeker Profile

A Job Seeker profile may contain:

* Full name
* Profile picture
* Bio
* Experience
* Skills
* Resume

---

# 5. Employer

An Employer is a User who can manage companies and publish jobs.

An Employer can:

* Create companies
* Manage companies
* Create jobs
* Edit jobs
* Close jobs
* View applicants
* Review applications
* Accept applications
* Decline applications with a reason

One User can own multiple Companies.

```text
User
├── Company A
│   ├── Job 1
│   └── Job 2
│
├── Company B
│   └── Job 3
│
└── Company C
    └── Job 4
```

---

# 6. Company

A Company represents the organization publishing jobs.

## Company Information

A Company contains:

* Name
* Description
* Logo
* Website
* Location
* Industry

One Company can publish multiple Jobs.

```text
Company
├── Job 1
├── Job 2
└── Job 3
```

---

# 7. Jobs

A Job is an employment opportunity published by a Company.

## Job Information

A Job contains:

* Title
* Description
* Requirements
* Required skills
* Experience level
* Location
* Work type
* Employment type
* Salary
* Application deadline
* Status
* Created date

## Experience Levels

Possible experience levels:

* Entry Level
* Junior
* Mid Level
* Senior

## Work Types

Possible work types:

* Remote
* Hybrid
* On-site

## Employment Types

Possible employment types:

* Full-time
* Part-time
* Contract
* Internship

---

# 8. Salary Rules

The Employer has three salary options.

## Option 1 Negotiable / Not Disclosed

```text
Salary: Negotiable
```

No fixed salary amount is required.

## Option 2 Fixed Salary, Negotiation Allowed

```text
Salary: $2,000/month
Negotiable: Yes
```

## Option 3 Fixed Salary, No Negotiation

```text
Salary: $2,000/month
Negotiable: No
```

Important validation rules:

```text
If salary is fixed:
    salary amount is required

If salary is negotiable without a fixed amount:
    salary amount may be empty
```

---

# 9. Job Status

A Job should not normally be deleted when the Employer no longer wants new applications.

The normal flow is:

```text
OPEN
  ↓
CLOSED
```

When a Job is closed:

* New applications are not allowed
* Existing applications remain
* The Employer can still review existing applicants
* Job history is preserved

Example:

```text
Job: Backend Developer
Status: CLOSED

Existing Applications:
├── Applicant 1
├── Applicant 2
└── Applicant 3
```

---

# 10. Job Seeker Job Flow

```text
Visitor
    ↓
Landing Page
    ↓
Register
    ↓
Create Account
    ↓
Job Seeker Dashboard
    ↓
Browse Jobs
    ↓
View Job Details
    ↓
Apply
    ↓
Application Submitted
    ↓
Employer Reviews
    ↓
Accepted / Declined
```

---

# 11. Job Detail Page

The Job Seeker should see enough information to decide whether the job is suitable.

The page should include:

* Job title
* Company information
* Location
* Work type
* Employment type
* Salary information
* Job description
* Requirements
* Required skills
* Experience level
* Application deadline
* Apply button

```text
[ APPLY NOW ]
```

---

# 12. Applications

An Application connects a Job Seeker to a Job.

```text
Job Seeker
    ↓
Application
    ↓
Job
```

An Application contains:

* Job Seeker
* Job
* Cover letter
* Resume
* Status
* Employer decision reason
* Created date
* Updated date

## Application Status

The application lifecycle is:

```text
SUBMITTED
    ↓
UNDER REVIEW
    ↓
ACCEPTED
```

or:

```text
SUBMITTED
    ↓
UNDER REVIEW
    ↓
DECLINED
```

If an application is declined:

```text
Status: DECLINED
Reason: Required
```

The reason should be stored and shown to the Job Seeker.

---

# 13. Job Seeker Application Dashboard

The Job Seeker can open:

```text
My Applications
```

Each application can show:

```text
Job Title
Company
Application Date
Status
```

Possible statuses:

```text
Under Review
Accepted
Declined
```

If declined:

```text
Reason:
[Employer's explanation]
```

---

# 14. Employer Applicant Management

The Employer can open:

```text
Menu
  ↓
Applicants
```

The Employer can see applicants grouped by Job:

```text
My Jobs
    ↓
Backend Developer
    ↓
Applicants
```

An Applicant card may show:

* Full name
* Experience
* Application date
* Application status

The Employer can then view:

* Applicant profile
* Experience
* Skills
* Resume
* Cover letter

The Employer can:

```text
[ ACCEPT ]
[ DECLINE ]
```

If declining:

```text
Reason required
```

---

# 15. Responsive UI

The application must work on mobile and desktop.

## Mobile

Jobs appear one per line:

```text
[ Job 1 ]

[ Job 2 ]

[ Job 3 ]
```

## Desktop

Jobs can expand into multiple columns:

```text
[ Job 1 ] [ Job 2 ] [ Job 3 ]

[ Job 4 ] [ Job 5 ] [ Job 6 ]
```

The layout should be responsive and able to adapt to different screen sizes.

---

# 16. MVP Features

## Authentication

* Registration
* Login
* Logout

## Job Seeker

* Profile
* Browse jobs
* Search jobs
* Filter jobs
* View job details
* Apply for jobs
* View applications
* Track application status

## Employer

* Become an Employer
* Create Company
* Edit Company
* Create Job
* Edit Job
* Close Job
* View Applicants
* Review Applications
* Accept Application
* Decline Application with Reason

---

# 17. Features After MVP

These are not part of the first version.

## Advanced Search

* Search by job title
* Search by skill
* Search by company
* Search by location

## Advanced Filtering

* Salary
* Experience
* Work type
* Employment type
* Industry

## Saved Jobs

Job Seekers can save jobs for later.

## Notifications

Examples:

* Application submitted
* Application accepted
* Application declined
* New applicant

This will later help us learn:

* Django Signals
* Celery
* Redis

## Company Reviews

Job Seekers can review Companies.

## Employer Teams

A Company can have:

* Owner
* HR Manager
* Recruiter

## Messaging

Employer and Job Seeker messaging.

---

# 18. Core Domain

```text
User
│
├── Job Seeker
│     │
│     └── Applications
│
└── Employer
      │
      └── owns multiple Companies
             │
             └── each Company has multiple Jobs
                    │
                    └── each Job has multiple Applications
```

The core relationships are:

```text
User
  │
  ├── owns many Companies
  │
  └── submits many Applications

Company
  │
  └── has many Jobs

Job
  │
  └── has many Applications

Application
  │
  ├── belongs to one Job Seeker
  └── belongs to one Job
```

---

# 19. Core Business Loop

```text
┌──────────────┐
│    USER      │
└──────┬───────┘
       │
       ├─────────────────┐
       │                 │
       ▼                 ▼
 JOB SEEKER          EMPLOYER
       │                 │
       │                 ▼
       │              COMPANY
       │                 │
       │                 ▼
       │                JOB
       │                 │
       └───────┐   ┌─────┘
               ▼   ▼
            APPLICATION
                 │
                 ▼
             REVIEW
            /       \
           ▼         ▼
       ACCEPTED    DECLINED
                    + REASON
```

This is the heart of the Job Board.

---

# 20. Next Architecture Stage

Before writing Django models, we will design the database relationships carefully.

We will determine:

* One-to-one relationships
* One-to-many relationships
* Many-to-many relationships
* Foreign keys
* Business rules
* Validation rules

The next step is to design the database relationships for:

```text
User
Profile
Company
Job
Application
```

We will design them one relationship at a time before writing code.
