import pytest
from fixtures import auth_client
from users.models import User
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db

class TestEndpoints():

    def test_login_success(self):
        client = APIClient()
        response = client.post("/authentication/register/",{"username":"asdfasdf","email":"asdfadfsd@gmail.com","password":"asdfasdf1!","password2":"asdfasdf1!"})
        response = client.post("/authentication/login/",{
            "username" : "asdfasdf",
            "password":"asdfasdf1!"
        })
        return response.status_code == 200

    def test_login_fail(self):
        client = APIClient()
        response = client.post("/authentication/login/",{
            "username" : "asdfasdf",
            "password" : "asdfasdf1"
        })
        return response.status_code == 403

    def test_register_success(self):
        client = APIClient()
        response = client.post("/authentication/register/",{"username":"asdfasdf","email":"asdfadfsd@gmail.com","password":"asdfasdf1!","password2":"asdfasdf1!"})
        assert response.status_code == 200

    def test_register_fail(self):
        client = APIClient()
        response = client.post("/authentication/register/",{"username":"","password":"asdfasdf1"})
        assert response.status_code == 400
