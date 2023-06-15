from django.urls import reverse
from rest_framework.test import APITestCase
from main import views as main_views
from main import settings as main_settings


class ClientAPITest(APITestCase):
    def setUp(self):
        self.status = main_views.statusAdminSeed()
        self.buttons = main_views.buttonSeed()
        self.contents = main_views.contentSeed()
        self.processes = main_views.processAdminSeed()
        self.departments = main_views.departmentSeed()
        self.problems = main_views.problemSeed()
        self.disparities = main_views.disparitySeed()
        self.admins = main_views.adminSeed()
        self.clients = main_views.clientSeed()

        self.auth_token = main_settings.DEFAULT_AUTH_TOKEN
        self.authentication(self.auth_token)

    def authentication(self, token):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

    def fail_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token 12341235')

    # api
    def test_get_statuses(self):
        response = self.client.get(reverse('api:buttons'))
        self.assertEqual(response.status_code, 200)

    def test_get_clients(self):
        response = self.client.get(reverse('api:clients'))
        self.assertEqual(response.status_code, 200)

    def test_get_departments(self):
        response = self.client.get(reverse('api:departments'))
        self.assertEqual(response.status_code, 200)

    def test_get_disparities(self):
        response = self.client.get(reverse('api:disparities'))
        self.assertEqual(response.status_code, 200)

    def test_get_problems(self):
        response = self.client.get(reverse('api:problems'))
        self.assertEqual(response.status_code, 200)

    def test_get_processes(self):
        response = self.client.get(reverse('api:processes'))
        self.assertEqual(response.status_code, 200)

    def test_get_regions(self):
        response = self.client.get(reverse('api:regions'))
        self.assertEqual(response.status_code, 200)

    def test_get_contents(self):
        response = self.client.get(reverse('api:contents'))
        self.assertEqual(response.status_code, 200)
