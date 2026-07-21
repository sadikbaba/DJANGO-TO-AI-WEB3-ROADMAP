from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Company(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    description = models.TextField()
    logo = models.ImageField(upload_to="company_logos/", blank=True)

    website = models.URLField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    industry = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# ====================== CHOICES ======================


class ExperienceLevel(models.TextChoices):
    ENTRY = "entry", "Entry Level"
    JUNIOR = "junior", "Junior"
    MID = "mid", "Mid Level"
    SENIOR = "senior", "Senior"


class WorkType(models.TextChoices):
    REMOTE = "remote", "Remote"
    ONSITE = "onsite", "On-site"
    HYBRID = "hybrid", "Hybrid"


class EmploymentType(models.TextChoices):
    FULL_TIME = "full_time", "Full Time"
    PART_TIME = "part_time", "Part Time"
    CONTRACT = "contract", "Contract"
    INTERNSHIP = "internship", "Internship"


class JobStatus(models.TextChoices):
    OPEN = "open", "Open"
    CLOSED = "closed", "Closed"


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    skills = models.TextField()
    location = models.CharField(max_length=200, blank=True)
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    salary_negotiable = models.BooleanField(default=False)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    experience_level = models.CharField(max_length=20, choices=ExperienceLevel.choices)

    work_type = models.CharField(max_length=20, choices=WorkType.choices)
    employment_type = models.CharField(max_length=20, choices=EmploymentType.choices)
    status = models.CharField(max_length=20, choices=JobStatus.choices)

    def __str__(self):
        return self.title

    def clean(self):

        if self.salary is None and self.salary_negotiable is False:
            raise ValidationError(
                "Salary must be provided when negotiation is not allowed."
            )


class ApplicationStatus(models.TextChoices):
    SUBMITTED = "submitted", "Submitted"
    UNDER_REVIEW = "under_review", "Under Review"
    ACCEPTED = "accepted", "Accepted"
    DECLINED = "declined", "Declined"


class Application(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    cover_letter = models.TextField(blank=True)
    decline_reason = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=20,
        choices=ApplicationStatus.choices,
        default=ApplicationStatus.SUBMITTED,
    )

    def clean(self):
        if self.status == ApplicationStatus.DECLINED and not self.decline_reason:
            raise ValidationError(
                "Please provide a reason when declining an application."
            )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["applicant", "job"], name="unique_application_per_user"
            )
        ]

    def __str__(self):
        return f"{self.applicant.username} - {self.job.title}"
