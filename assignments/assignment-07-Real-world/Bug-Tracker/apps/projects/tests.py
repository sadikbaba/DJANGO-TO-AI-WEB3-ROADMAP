from django.test import TestCase, Client
from .models import Project
from apps.accounts.models import User
from django.urls import reverse

# Create your tests here.


class ProjectModelTests(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="testuser", email="testmail@gmail.com", password="testpassword123"
        )
        self.project = Project.objects.create(
            owner=self.user,
            name="Hospital Management",
            description="Final Year Project",
        )

    def test_project_created_successful(self):

        self.assertEqual(self.project.name, "Hospital Management")
        self.assertEqual(self.project.owner, self.user)
        self.assertEqual(self.project.description, "Final Year Project")

    def test_return_project_name(self):

        self.assertEqual(str(self.project), self.project.name)


class ProjectViewTests(TestCase):

    def setUp(self):

        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", email="testmail@gmail.com", password="testpassword123"
        )
        self.client.login(username=self.user.username, password="testpassword123")

    def test_user_can_create_project(self):

        response = self.client.post(
            reverse("projects:create"),
            data={
                "name": "Bug Tracker",
                "description": "Backend Project",
            },
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            Project.objects.filter(name="Bug Tracker", owner=self.user).exists()
        )

    def test_user_cannot_view_another_users_project(self):

        other_user = User.objects.create_user(
            username="fatima", email="fatima@example.com", password="StrongPassword123!"
        )

        other_project = Project.objects.create(
            owner=other_user,
            name="Secret Project",
            description="Top Secret",
        )

        response = self.client.get(
            reverse(
                "projects:detail",
                kwargs={"pk": other_project.pk},
            )
        )

        self.assertEqual(response.status_code, 404)

    def test_user_can_edit_own_project(self):
        """
        Test:
        A logged-in user can edit their own project.
        """

        project = Project.objects.create(
            owner=self.user,
            name="Old Project",
            description="Old Description",
        )

        response = self.client.post(
            reverse(
                "projects:edit",
                kwargs={"pk": project.pk},
            ),
            {
                "name": "New Project",
                "description": "New Description",
            },
        )

        project.refresh_from_db()

        self.assertEqual(
            response.status_code,
            302,
        )

        self.assertEqual(
            project.name,
            "New Project",
        )

        self.assertEqual(
            project.description,
            "New Description",
        )

    def test_user_cannot_edit_another_users_project(self):
        """
        Test:
        A logged-in user cannot edit another user's project.
        """

        other_user = User.objects.create_user(
            username="fatima", email="fatima@example.com", password="StrongPassword123!"
        )

        other_project = Project.objects.create(
            owner=other_user,
            name="Secret Project",
            description="Top Secret",
        )

        response = self.client.post(
            reverse(
                "projects:edit",
                kwargs={"pk": other_project.pk},
            ),
            {
                "name": "Hacked Project",
                "description": "Hacked Description",
            },
        )

        other_project.refresh_from_db()

        self.assertEqual(
            response.status_code,
            404,
        )

        self.assertEqual(
            other_project.name,
            "Secret Project",
        )

        self.assertEqual(
            other_project.description,
            "Top Secret",
        )
