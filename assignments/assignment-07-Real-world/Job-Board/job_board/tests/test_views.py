from django.test import TestCase, Client
from job_board.views import company_list_view


class CompanyViewTest(TestCase):

    def test_company_list_page_loads(self):

        client = Client()
        response = client.get("/companies/")

        self.assertEqual(response.status_code, 200)

    def test_company_create_requires_login(self):
        client = Client()

        response = client.get("/companies/create/")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login/?next=/companies/create/")
