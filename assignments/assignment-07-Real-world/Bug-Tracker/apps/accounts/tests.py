from django.test import TestCase, Client
from django.urls import reverse

from apps.accounts.models import User, Profile


class LoginViewTest(TestCase):

    def setUp(self):
        """
        Runs before every test.

        We create:
        1. A fake browser (Client)
        2. A user that already exists in the database
        """

        self.client = Client()

        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="RealPassword123!"
        )

    def test_user_can_login_successfully(self):
        """
        Test:
        A user enters the correct username and password.

        Expected:
        - Login succeeds.
        - User is redirected to the home page.
        """

        response = self.client.post(
            reverse("accounts:login"),
            data={
                "username": "testuser",
                "password": "RealPassword123!",
            },
        )

        # A successful login redirects the user.
        self.assertEqual(response.status_code, 302)

        # Check the redirect destination.
        self.assertRedirects(response, reverse("core:dashboard"))

    def test_login_fails_with_wrong_password(self):
        """
        Test:
        User enters the correct username but wrong password.

        Expected:
        - Stay on login page.
        - Show an error message.
        """

        response = self.client.post(
            reverse("accounts:login"),
            data={
                "username": "testuser",
                "password": "WrongPassword",
            },
        )

        # No redirect because login failed.
        self.assertEqual(response.status_code, 200)

        # Check the error message appears.
        self.assertContains(response, "Username or password is incorrect.")

    def test_login_fails_with_empty_fields(self):
        """
        Test:
        User submits an empty form.

        Expected:
        - Stay on login page.
        - Required field errors appear.
        """

        response = self.client.post(
            reverse("accounts:login"),
            data={
                "username": "",
                "password": "",
            },
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Please enter your username.")
        self.assertContains(response, "Please enter your password")


class ProfileModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test_mail@gmail.com", password="testpassword123"
        )

    def test_profile_created(self):

        profile_exists = Profile.objects.filter(user=self.user).exists()

        self.assertTrue(profile_exists)
