from django.test import TestCase
from job_board.models import (
    Company,
    User,
    Application,
    Job,
    ExperienceLevel,
    WorkType,
    EmploymentType,
    JobStatus,
    ApplicationStatus,
)
from django.db import IntegrityError
from django.core.exceptions import ValidationError


class CompanyModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="sadik", email="sadik@gmail.com", password="12345678"
        )
        self.company = Company.objects.create(owner=self.user, name="Sadik company")

    def test_company_returns_name(self):
        company_name = str(self.company)
        self.assertEqual(company_name, "Sadik company")

    def test_company_saved_in_data_base(self):
        self.assertEqual(Company.objects.count(), 1)


class ApplicationModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="sadik", email="sadik@gmail.com", password="testpassword123"
        )
        self.company = Company.objects.create(
            owner=self.user,
            name="sadik company",
        )
        self.job = Job.objects.create(
            company=self.company,
            title="AI writer",
            description="for writers",
            requirements="good at AI",
            skills="most know python",
            salary_negotiable=False,
            salary=200,
            experience_level=ExperienceLevel.ENTRY,
            work_type=WorkType.REMOTE,
            employment_type=EmploymentType.FULL_TIME,
            status=JobStatus.OPEN,
        )

    def test_user_cannot_apply_twice(self):
        Application.objects.create(applicant=self.user, job=self.job)

        with self.assertRaises(IntegrityError):
            Application.objects.create(applicant=self.user, job=self.job)

    def test_cannot_decline_without_reason(self):
        application = Application(
            applicant=self.user,
            job=self.job,
            status=ApplicationStatus.DECLINED,
            decline_reason="",  # empty reason
        )

        with self.assertRaises(ValidationError):
            application.clean()
