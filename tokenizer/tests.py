from django.test import TestCase
from rest_framework.test import APIClient
from User.models import User
from django.urls import reverse
from tokenizer.payload import user_payload
import pytest

@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    return User.objects.create_user(email="tester@mail.com", password="tester@123")

def test_token_creation(api_client, user):
    url=reverse('token_create')
    response = api_client.post(url, user_payload)
    assert response.status_code == 200

    assert 'access' in response.data
    assert 'refresh' in response.data