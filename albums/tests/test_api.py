from rest_framework.test import APIClient
import pytest
from fixtures.auth_client import auth_client
pytestmark = pytest.mark.django_db
from artists.models import Artist 
from artists.serializers.ArtistSerializer import ArtistSerializer
class TestAlbumAPI():

    def test_get_method(self):
        client = APIClient()
        response = client.get("/albums/")
        assert response.status_code == 200
    
    def test_post_with_wrong_data (self):
        client = APIClient()
        response = client.post("/albums/create/")
        assert response.status_code == 400
    
    def test_post_with_correct_data(self,auth_client):
        artist = ArtistSerializer(data={"stageName":"TestName" , "socialLink":"https://www.facebook.com/"})
        if artist.is_valid():
            artist.save()
        else :
            print(artist.errors)
            assert False
        response = auth_client.post("/albums/create/",{
            "name" : "asdasfsdf",
            "artist" : artist.data['id'],
            "cost" : "1000",
            "releaseDate" : "2022-11-02T23:34:15.15165"
        },format="json")
        assert response.status_code == 201
