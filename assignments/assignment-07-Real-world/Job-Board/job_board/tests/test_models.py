from django.test import TestCase
from job_board.models import Company, User


class CompanyModelTest(TestCase):
    def test_company_returns_name(self):
        user = User.objects.create_user(
            username="sadik", email="sadik@gmail.com", password="12345678"
        )
        company = Company.objects.create(owner=user, name="Sadik company")

        company_name = str(company)
        self.assertEqual(company_name, "Sadik company")

    def test_company_saved_in_data_base(self):
        user = User.objects.create_user(
            username="sadik", email="sadik@gmail.com", password="12345678"
        )
        Company.objects.create(owner=user, name="Sadik company")

        self.assertEqual(Company.objects.count(), 1)
