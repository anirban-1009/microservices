from django.test import TestCase
from rest_framework.test import APIClient
from user_mgmt.views import UsersListViewSet, UsersDetailViewSet
from User.models import User
from user_mgmt.serializers import UsersSerializer
from user_mgmt.payloads import create_user_payload

class UsersListViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.viewset = UsersListViewSet()

    def test_list_user(self):
        response = self.client.get('/users/list/')
        users = UsersSerializer(User.objects.all(), many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, users.data)

    def test_create_user(self):
        response = self.client.post('/users/list/', create_user_payload)
        self.assertEqual(response.status_code, 201)
        return response.json().get('id')

class UsersDetailViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.viewset = UsersDetailViewSet()
        self.user_id = UsersListViewSetTest.test_create_user(self)

    def test_detail_user(self):
        response = self.client.get(f'users/list/1/')
        print(response)
        user = UsersSerializer(User.objects.get(id=self.user_id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, user.data)