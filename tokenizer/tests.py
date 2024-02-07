from rest_framework.test import APIClient
from User.models import User
import pytest
from rest_framework.authtoken.models import Token
from tokenizer.serializer import TokensListSerializers


@pytest.fixture
def user():
    return User.objects.create_user(email="tester@mail.com", password="tester@123")

@pytest.mark.django_db
def test_token_list(client):
    url='/token/list/'
    tokens = TokensListSerializers(Token.objects.all())
    response = client.get(url)
    response = response.json()
    print('*'*10)
    print(response)
    assert response == None