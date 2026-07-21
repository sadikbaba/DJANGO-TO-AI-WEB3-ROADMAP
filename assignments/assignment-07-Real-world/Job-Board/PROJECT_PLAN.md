# Job Board --- Project Plan

## Project Strategy

We will plan the complete project before writing the first feature.

The project will be developed in a backend-first order, but not in a way
that ignores the frontend.

The preferred architecture is:

``` text
Requirements
    ↓
Domain design
    ↓
Models
    ↓
Migrations
    ↓
Forms / validation
    ↓
Business logic
    ↓
Views
    ↓
URLs
    ↓
Templates
    ↓
CSS
    ↓
Tests
    ↓
Security review
    ↓
Performance review
```

The reason for starting with the backend is that the backend defines the
data and rules of the application.

The frontend is the user interface for those rules.

------------------------------------------------------------------------

# PHASE 0 --- Planning and Architecture

Before writing code:

-   Understand what a job board is.
-   Define user roles.
-   Define the main features.
-   Define the data relationships.
-   Decide the application structure.
-   Decide what belongs in each Django app.
-   Decide the first MVP.
-   Identify future features.

Possible app structure:

``` text
job_board/
│
├── config/
│
├── accounts/
│
├── jobs/
│
├── companies/
│
├── applications/
│
└── core/
```

We should not create unnecessary apps just for the sake of creating
apps.

The final structure should be decided based on domain responsibility.

------------------------------------------------------------------------

# PHASE 1 --- Authentication and User Roles

First establish the foundation.

Features:

-   Registration.
-   Login.
-   Logout.
-   Password recovery.
-   User profile basics.
-   User role concept.

Possible roles:

``` text
JOB_SEEKER
EMPLOYER
```

Important design decision:

The role system must be designed carefully.

We should decide whether to use:

-   A profile model with a role.
-   Django Groups and Permissions.
-   A combination.

The choice should be explained before implementation.

------------------------------------------------------------------------

# PHASE 2 --- Employer and Company Domain

An employer needs an identity beyond a normal user account.

Features:

-   Company profile.
-   Company name.
-   Description.
-   Website.
-   Location.
-   Logo.
-   Company owner.

Relationship:

``` text
User
  │
  │ owns
  ▼
Company
  │
  │ publishes
  ▼
Jobs
```

Security rule:

Only the appropriate employer should be able to manage their company.

------------------------------------------------------------------------

# PHASE 3 --- Job Domain

This is the core of the project.

Design the Job model before writing it.

Possible job information:

-   Title.
-   Description.
-   Company.
-   Location.
-   Remote/hybrid/on-site status.
-   Employment type.
-   Salary information.
-   Required skills.
-   Experience level.
-   Status.
-   Created date.
-   Updated date.
-   Deadline.

Possible status:

``` text
DRAFT
PUBLISHED
CLOSED
```

We should think carefully about whether all of these belong in the first
version.

The goal is to design a realistic but manageable MVP.

------------------------------------------------------------------------

# PHASE 4 --- Job Creation and Management

Employer workflow:

``` text
Employer
    ↓
Create job
    ↓
Validate data
    ↓
Save job
    ↓
Publish job
    ↓
Edit job
    ↓
Close job
```

Features:

-   Create job.
-   Edit job.
-   Delete or archive job.
-   Publish job.
-   Close job.
-   Ownership security.

Security test:

``` text
Employer A
    ↓
Attempts to edit
    ↓
Employer B's job
```

Expected:

``` text
DENIED
```

------------------------------------------------------------------------

# PHASE 5 --- Job Browsing

Job seekers need to discover jobs.

Features:

-   Job list.
-   Job detail page.
-   Pagination.
-   Empty states.
-   Responsive design.

Basic flow:

``` text
Job list
    ↓
Click job
    ↓
Job detail
    ↓
Apply
```

This is where performance concerns begin to matter.

We should think about:

-   Number of database queries.
-   Pagination.
-   Related company data.
-   N+1 queries.

------------------------------------------------------------------------

# PHASE 6 --- Search and Filtering

Search features:

-   Search by title.
-   Search by location.
-   Search by company.
-   Filter by employment type.
-   Filter by remote status.
-   Filter by experience level.

Before implementing, understand:

``` text
User input
    ↓
Query parameters
    ↓
Validated filters
    ↓
Database query
    ↓
Results
```

Security and performance must be considered.

------------------------------------------------------------------------

# PHASE 7 --- Applications

Job seeker workflow:

``` text
Open job
    ↓
Click Apply
    ↓
Submit application
    ↓
Application stored
    ↓
Employer sees application
```

Application data may include:

-   Applicant.
-   Job.
-   Cover letter.
-   Resume.
-   Status.
-   Created date.
-   Updated date.

Possible status:

``` text
SUBMITTED
REVIEWING
SHORTLISTED
REJECTED
ACCEPTED
```

Important business rules:

-   A user should not apply to the same job multiple times unless
    explicitly allowed.
-   Closed jobs should not accept applications.
-   Only the applicant should see their private application data.
-   Only the employer responsible for the job should manage its
    applications.

------------------------------------------------------------------------

# PHASE 8 --- Employer Application Management

Employer workflow:

``` text
Employer
    ↓
Opens job
    ↓
Views applicants
    ↓
Reviews application
    ↓
Changes status
```

Security:

``` text
Employer A
    ↓
Attempts to view
    ↓
Employer B's applications
```

Must be denied.

------------------------------------------------------------------------

# PHASE 9 --- Caching

Now introduce caching where the application actually has something worth
caching.

Learn:

-   Cache basics.
-   Cache keys.
-   Expiration.
-   Cache invalidation.
-   Redis cache backend.

Possible caching targets:

-   Popular job listings.
-   Search results.
-   Company information.
-   Frequently accessed job detail pages.

We will first measure and understand the problem before adding caching.

------------------------------------------------------------------------

# PHASE 10 --- Django Signals

Use signals only where they make architectural sense.

Possible uses:

-   Automatically creating a profile.
-   Triggering an event after a model is created.
-   Audit-related behavior.

We will also discuss when signals are a bad choice.

------------------------------------------------------------------------

# PHASE 11 --- Celery + Redis

Introduce asynchronous work.

Possible tasks:

-   Send application confirmation email.
-   Notify employer about a new application.
-   Send status-change emails.
-   Scheduled cleanup.
-   Background processing.

Architecture:

``` text
Django
    ↓
Creates task
    ↓
Redis broker
    ↓
Celery worker
    ↓
Executes task
```

We will learn:

-   Tasks.
-   Workers.
-   Queues.
-   Retries.
-   Failures.
-   Idempotency.

------------------------------------------------------------------------

# PHASE 12 --- Testing

Testing should exist throughout development.

Test categories:

## Model Tests

-   Valid job creation.
-   Invalid data.
-   Relationships.
-   Constraints.

## Form Tests

-   Required fields.
-   Validation.
-   Invalid input.

## View Tests

-   Anonymous access.
-   Authenticated access.
-   Correct response.
-   Redirects.

## Security Tests

-   Ownership.
-   Permissions.
-   Unauthorized URL access.

## Application Tests

-   Duplicate applications.
-   Closed job applications.
-   Employer management.

## Task Tests

-   Task behavior.
-   Retry behavior where appropriate.

------------------------------------------------------------------------

# PHASE 13 --- Security Best Practices

Perform a systematic security review.

Checklist:

-   Authentication.
-   Authorization.
-   Ownership checks.
-   CSRF.
-   XSS.
-   SQL injection.
-   File upload validation.
-   Secure cookies.
-   Secret management.
-   Debug settings.
-   Error exposure.
-   Sensitive information.
-   Rate limiting concepts.

Threat-model question:

> What can a normal user do that they should not be able to do?

------------------------------------------------------------------------

# PHASE 14 --- Performance Optimization

Measure first.

Potential areas:

-   N+1 queries.
-   Missing indexes.
-   Unnecessary database queries.
-   Large result sets.
-   Missing pagination.
-   Expensive search.
-   Repeated queries.

Tools and techniques:

-   Django Debug Toolbar.
-   Query counting.
-   `select_related`.
-   `prefetch_related`.
-   Indexes.
-   Pagination.
-   Caching.

Optimization flow:

``` text
Find bottleneck
    ↓
Measure it
    ↓
Understand it
    ↓
Change one thing
    ↓
Measure again
```

------------------------------------------------------------------------

# PHASE 15 --- Final Production-Style Review

Before considering the project complete:

-   Run the test suite.
-   Review security.
-   Review permissions.
-   Review database queries.
-   Review caching.
-   Review background tasks.
-   Review error handling.
-   Review UI responsiveness.
-   Review code organization.
-   Review deployment readiness.

------------------------------------------------------------------------

# Recommended Development Order

The most important order is:

``` text
1. Plan the domain
2. Design models
3. Build authentication foundation
4. Build company/employer domain
5. Build jobs
6. Build job management
7. Build browsing
8. Build search/filtering
9. Build applications
10. Build employer application management
11. Add caching
12. Add signals where appropriate
13. Add Celery + Redis
14. Expand testing
15. Security review
16. Performance optimization
17. Final production review
```

This order lets us learn the advanced Phase 7 topics through a real
application instead of studying them as disconnected theory.