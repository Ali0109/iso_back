from django.urls import reverse
from rest_framework.test import APITestCase
from .. import models
from main import views as main_views
from main import settings as main_settings


class ClientAPITest(APITestCase):
    def setUp(self):
        main_views.statusAdminSeed()
        main_views.buttonSeed()
        main_views.contentSeed()
        main_views.processAdminSeed()
        main_views.regionSeed()
        main_views.shopSeed()
        main_views.departmentSeed()
        main_views.problemSeed()
        main_views.disparitySeed()
        main_views.adminSeed()
        main_views.clientSeed()

        self.auth_token = main_settings.DEFAULT_AUTH_TOKEN
        self.authentication(self.auth_token)

    def authentication(self, token):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

    def fail_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token 12341235')

    # api
    def test_client_list(self):
        response = self.client.get(reverse('api:clients/'))
        self.assertEqual(response.status_code, 200)

