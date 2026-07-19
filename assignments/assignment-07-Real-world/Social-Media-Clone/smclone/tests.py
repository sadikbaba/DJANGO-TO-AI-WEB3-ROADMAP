from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from .models import UsernameRecoveryCode

# Create your tests here.


class VerifyUsernameTest(TestCase):

    def test_valid_otp_shows_username(self):

        user = User.objects.create_user(
            username="testuser", email="test@example.com", password="TestPassword123"
        )

        recovery_code = UsernameRecoveryCode.objects.create(
            user=user, code="123456", expires_at=timezone.now() + timedelta(minutes=5)
        )

        session = self.client.session

        session["username_recovery_code_id"] = recovery_code.id

        session.save()

        response = self.client.post(reverse("Verify_username"), {"code": "123456"})

        self.assertContains(response, "testuser")

    def test_invalid_otp_is_rejected(self):

        user = User.objects.create_user(
            username="testuser", email="test@example.com", password="TestPassword123"
        )

        recovery_code = UsernameRecoveryCode.objects.create(
            user=user, code="123456", expires_at=timezone.now() + timedelta(minutes=5)
        )

        session = self.client.session

        session["username_recovery_code_id"] = recovery_code.id

        session.save()

        response = self.client.post(reverse("Verify_username"), {"code": "999999"})

        self.assertContains(response, "Invalid recovery code.")

    def test_valid_user_recovery(self):

        user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="TestPassword123",
        )

        recovery_code = UsernameRecoveryCode.objects.create(
            user=user, code="123456", expires_at=timezone.now() + timedelta(minutes=5)
        )

        session = self.client.session

        session["username_recovery_code_id"] = recovery_code.id

        session.save()

        response = self.client.post(reverse("Verify_username"), {"code": "123456"})

        self.assertContains(response, user.username)
