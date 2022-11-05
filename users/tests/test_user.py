import pytest
from fixtures.auth_client import auth_client
from rest_framework.test import APIClient
from users.models import User

pytestmark = pytest.mark.django_db

class TestUser():
    def test_get_method(self,auth_client):
        response = auth_client.get("/users/1/")
        assert response.status_code == 200
        data = response.data 
        user = User.objects.get(id=1)
        assert data['username'] == user.username 
        assert data['email'] == user.email  
        assert data['bio'] == user.bio

    def test_put_method(self,auth_client):
        response = auth_client.put("/users/1/",{
            "username":"Update",
            "email" : "asdfasdf@gmail.com",
            "bio" : "Success"
        })
        assert response.status_code == 201
        user = User.objects.get(id=1)
        assert user.bio == "Success"
        assert user.username == "Update"
        assert user.email == "asdfasdf@gmail.com"

    def test_patch_method(self,auth_client):
        response = auth_client.patch("/users/1/",{
            "username" : "updatedUserName",
        })
        assert response.status_code == 201
        user = User.objects.get(id=1)
        assert user.username == "updatedUserName"
