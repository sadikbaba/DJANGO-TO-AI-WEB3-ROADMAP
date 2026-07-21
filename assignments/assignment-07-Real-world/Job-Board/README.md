# Job Board --- Real-World Django Project

## Project Purpose

This project is the second major project in my Django Phase 7 ---
Real-World Django learning journey.

The goal is not simply to copy a tutorial. I want to build a realistic
Job Board while learning and applying:

-   Caching
-   Django Signals
-   Celery + Redis
-   Testing
-   Security Best Practices
-   Performance Optimization

------------------------------------------------------------------------

# What Is a Job Board?

A Job Board is a platform where:

-   Employers or companies publish job vacancies.
-   Job seekers search and browse available jobs.
-   Job seekers view job details.
-   Job seekers apply for jobs.
-   Employers manage the jobs they posted.
-   Applications are stored and managed.

A simplified flow:

``` text
Employer
   ↓
Creates a job
   ↓
Job becomes available
   ↓
Job seeker searches for it
   ↓
Job seeker opens job details
   ↓
Job seeker applies
   ↓
Employer manages applications
```

The application has two main types of users:

## Job Seeker

A job seeker can:

-   Create an account.
-   Create and manage a profile.
-   Browse jobs.
-   Search jobs.
-   Filter jobs.
-   View job details.
-   Apply for jobs.
-   Track applications.

## Employer

An employer can:

-   Create an account.
-   Create a company profile.
-   Publish jobs.
-   Edit jobs.
-   Close jobs.
-   View applications.
-   Manage applicants.

A realistic job board is therefore a perfect project for learning
real-world Django architecture.

------------------------------------------------------------------------

# Core Learning Philosophy

I am not trying to memorize code.

I want to understand:

``` text
Requirement
    ↓
Database model
    ↓
Business logic
    ↓
View/API
    ↓
Template/UI
    ↓
Tests
    ↓
Security
    ↓
Performance
```

The mentor must:

1.  Teach one meaningful concept at a time.
2.  Explain WHY before HOW.
3.  Give me a task and let me write the code.
4.  Check my code after I submit it.
5.  Tell me exactly what is correct and what is wrong.
6.  Give hints before giving complete solutions.
7.  Only give the full solution when necessary.
8.  Never randomly jump ahead.
9.  Never rewrite working code unnecessarily.
10. Use analogies when a concept is difficult.

------------------------------------------------------------------------

# Technologies

The project is built with:

-   Python
-   Django
-   PostgreSQL
-   HTML
-   CSS
-   JavaScript only where genuinely useful
-   Redis
-   Celery

The UI should use custom CSS.

Do not use Bootstrap unless I explicitly request it.

------------------------------------------------------------------------

# Main Learning Topics

## 1. Caching

We will learn:

-   What caching is.
-   Why caching exists.
-   Cache invalidation.
-   Django cache framework.
-   Cache backends.
-   Redis caching.
-   View caching.
-   Low-level caching.
-   Caching query results.
-   When caching is useful.
-   When caching is dangerous.

Analogy:

``` text
Database = warehouse
Cache = items kept on the shop counter
```

The counter is faster, but it must be updated when the warehouse
changes.

------------------------------------------------------------------------

## 2. Django Signals

We will learn:

-   What signals are.
-   `pre_save`.
-   `post_save`.
-   `pre_delete`.
-   `post_delete`.
-   Why signals can be useful.
-   Why signals can make code difficult to understand.
-   When explicit service logic is better.

Signals should be used deliberately, not everywhere.

------------------------------------------------------------------------

## 3. Celery + Redis

We will learn:

``` text
Django
   ↓
Creates a task
   ↓
Redis
   ↓
Celery worker
   ↓
Executes task in background
```

Examples:

-   Sending emails.
-   Processing background work.
-   Scheduled tasks.
-   Notifications.
-   Long-running operations.

We will understand:

-   Broker.
-   Worker.
-   Task.
-   Queue.
-   Asynchronous execution.
-   Retries.
-   Failure handling.

------------------------------------------------------------------------

## 4. Testing

Testing will be part of development, not something added at the end.

We will test:

-   Models.
-   Forms.
-   Views.
-   Authentication.
-   Permissions.
-   Business logic.
-   Job applications.
-   Security-sensitive behavior.
-   Celery tasks where appropriate.

The pattern:

``` text
Write code
    ↓
Test code
    ↓
Break it intentionally
    ↓
Confirm the test catches the problem
    ↓
Fix the code
```

------------------------------------------------------------------------

## 5. Security Best Practices

We will actively review:

-   Authentication.
-   Authorization.
-   Ownership checks.
-   CSRF protection.
-   XSS prevention.
-   SQL injection protection.
-   File upload security.
-   Secure password handling.
-   Sensitive data exposure.
-   Rate limiting concepts.
-   Secure configuration.
-   Environment variables.

The most important question is:

> What happens if a malicious user changes the URL or sends a request
> manually?

------------------------------------------------------------------------

## 6. Performance Optimization

We will learn:

-   Query optimization.
-   `select_related`.
-   `prefetch_related`.
-   N+1 queries.
-   Database indexes.
-   Pagination.
-   Caching.
-   Efficient queries.
-   Measuring performance before optimizing.

Rule:

``` text
Measure first.
Optimize second.
```

------------------------------------------------------------------------

# Project Goals

The final Job Board should feel like a real application, not just a
collection of Django exercises.

The project should eventually support:

-   User registration and login.
-   Job seeker profiles.
-   Employer/company profiles.
-   Job creation.
-   Job editing.
-   Job closing.
-   Job browsing.
-   Search.
-   Filtering.
-   Pagination.
-   Job applications.
-   Application tracking.
-   Employer applicant management.
-   Background email tasks.
-   Caching.
-   Signals where appropriate.
-   Automated tests.
-   Security review.
-   Performance optimization.

------------------------------------------------------------------------

# Learning Rule

I write the code first.

The mentor should not immediately dump the answer.

Preferred flow:

``` text
1. Explain concept.
2. Explain WHY.
3. Show the goal.
4. Give me a task.
5. I write code.
6. I submit code.
7. Mentor reviews it.
8. Mentor says:
   - Correct
   - Incorrect
   - Partially correct
9. Give hints if needed.
10. I fix it.
11. Only then move forward.
```

This project is for becoming capable of building real Django systems
independently.