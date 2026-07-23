from django.test import TestCase
from job_board.forms import CompanyForm


class CompanyFormTest(TestCase):

    def test_company_form_is_valid(self):
        data = {
            "name": "sadik company",
            "description": "Web 3 and AI company",
            "industry": "AI/Web3 ",
        }

        form = CompanyForm(data)

        self.assertTrue(form.is_valid(), form.errors)

    def test_company_form_without_name_is_invalid(self):

        data = {
            "name": "",
            "description": "Web 3 and AI company",
            "industry": "AI/Web3 ",
        }

        form = CompanyForm(data)

        self.assertFalse(form.is_valid(), form.errors)
