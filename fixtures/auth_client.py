import pytest
from rest_framework.test import APIClient
from users.serializers import UserSerializer

@pytest.fixture
def auth_client(user = None):
    client = APIClient()
    if user is None:
        user = client.post("/authentication/register/",
            {"username":"asdfasdf",
            "email":"asdfadfsd@gmail.com",
            "password":"asdfasdf1!",
            "password2":"asdfasdf1!"})
    else :
        user = client.post("/authentication/register/",
            {"username":user['username'],
            "email":user['email'],
            "password":user['password'],
            "password2":user['password2']})
    client.post("/authentication/login/" , user)
    return client
    