import pytest
from users.models import User
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db

from users.serializers import UserSerializer

class TestEndpoints():

    def test_register_success(self):
        client = APIClient()
        response = client.post("/authentication/register/",{"username":"remarema","email":"asdfadfsd@gmail.com","password":"remarema1!","password2":"remarema1!"})
        assert response.status_code == 200
    
    def test_register_username_missing(self,auth_client):
        client , id= auth_client()
        payload = dict(
            email="remarema@email.com",
            password="remaremaF!",
            password2="remaremaF!"
        )
        response = client.post("/authentication/register/",payload)
        data = response.data 
        assert response.status_code == 400
        assert "username" in data
    
    def test_register_email_missing(self,auth_client):
        client , id= auth_client()
        payload = dict(
            username= "remarema",
            password="remaremaF!",
            password2="remaremaF!"
        )
        response = client.post("/authentication/register/",payload)
        data = response.data 
        assert response.status_code == 400
        assert "email" in data
    
    def test_register_password_missing(self,auth_client):
        client , id = auth_client()
        payload = dict(
            username= "remarema",
            email="remarema@email.com",
            password2="remaremaF!"
        )
        response = client.post("/authentication/register/",payload)
        data = response.data 
        assert response.status_code == 400
        assert "password" in data
    
    def test_register_password2_missing(self,auth_client):
        client , id = auth_client()
        payload = dict(
            username= "remarema",
            email="remarema@email.com",
            password= "remaremaF!",
        )
        response = client.post("/authentication/register/",payload)
        data = response.data 
        assert response.status_code == 400
        assert "password2" in data

    def test_register_passwords_not_match(self,auth_client):
        client , id = auth_client()
        payload = dict(
            username="qwerqwer",
            email = "qwerqwer@gmail.com",
            password1 = "reamream1!",
            password2 = "reamream1!!"
        )
        response = client.post("/authentication/register/",payload)
        assert response.status_code == 400
    
    def test_register_common_password(self,auth_client):
        client , _ = auth_client()
        payload = dict(
            username="asdfasdff",
            email="asdfasdfdf@gmail.com",
            password="123456789",
            password2 = "123456789"
        )
        response = client.post("/authentication/register/",payload)
        assert response.status_code == 400
    
    def test_register_invalid_mail(self,auth_client):
        client , _ = auth_client()
        payload = dict(
            username = "asdfasdfsdf",
            email = "asdfjjsdfiosdif",
            password = "asdfasdfF!",
            password2 = "asdfasdfF!"
        )
        response = client.post("/authentication/register/",payload)
        assert response.status_code == 400

    def test_register_uniqe_username(self,auth_client):
        client , _ = auth_client()
        payload = dict(
            username = "asdfasdf" ,# same as the user used in auth client
            email = "asdfmdlk@gmail.com",
            password= "asdfasdf!1",
            password2= "asdfasdf1!"
        )
        response = client.post("/authentication/register/",payload)
        assert response.status_code == 400

    def test_register_unique_email(self,auth_client):
        client, _ = auth_client()
        payload = dict(
            username = "asdfsdfasdfsd" ,# same as the user used in auth client
            email = "asdfasdf@gmail.com",
            password= "asdfasdf!1",
            password2= "asdfasdf1!"
        )
        response = client.post("/authentication/register/",payload)
        assert response.status_code == 400

    def test_login_success(self,user,auth_client):
        client , _ = auth_client()
        payload={
            "username" : "asdfasdf",
            "password" : "asdfasdF1!"
        }
        response = client.post("/authentication/login/",payload)
        assert response.status_code == 200
        data = response.data
        assert "token" in data
        assert "user" in data
        assert data['user']['username'] == user.username

    def test_login_fail(self,auth_client):
        client , _ = auth_client()
        payload = {
            "username" : "remarema",
            "password" : "remarema1"
        }
        response = client.post("/authentication/login/",payload)
        assert response.status_code == 403
    

    def test_logout_user(self,auth_client):
        client , _ = auth_client()
        response = client.post('/authentication/logout/')

        assert response.status_code == 204

    def test_logout_user_unauthenticated(self,client):
        response = client.post('/authentication/logout/')

        assert response.status_code == 401

    




    
