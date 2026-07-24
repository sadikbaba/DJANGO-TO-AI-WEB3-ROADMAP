from django.test import TestCase, Client
from job_board.views import company_list_view
from job_board.models import (
    User,
    Company,
    Job,
    Application,
    ExperienceLevel,
    WorkType,
    EmploymentType,
    JobStatus,
)
from django.urls import reverse


class CompanyViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_company_list_page_loads(self):

        client = Client()
        response = client.get("/companies/")

        self.assertEqual(response.status_code, 200)

    def test_company_create_requires_login(self):
        client = Client()

        response = client.get("/companies/create/")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login/?next=/companies/create/")


class ApplicationViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="sadik", email="sadik@gmail.com", password="testpassword123"
        )
        self.company = Company.objects.create(
            owner=self.user, name="sadik", description="Ai company", industry="Ai"
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

    def test_anonymous_user_redirected_to_login(self):

        response = self.client.get(reverse("application", args=[self.job.id]))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login/?next=/jobs/1/apply/")

    def test_logged_in_user_can_access_application_page(self):

        self.client.login(username=self.user.username, password="testpassword123")
        response = self.client.get(reverse("application", args=[self.job.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "job_board/application.html")

    def test_logged_in_user_and_create_application(self):

        self.client.login(username=self.user.username, password="testpassword123")
        response = self.client.post(
            reverse("application", args=[self.job.id]),
            data={
                "cover_letter": "I am very interested in this job.",
                # add other required fields if your form has them
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url,   reverse("jobs_detail", args=[self.job.id]))
        self.assertTrue(
            Application.objects.filter(applicant=self.user, job=self.job).exists()
        )
