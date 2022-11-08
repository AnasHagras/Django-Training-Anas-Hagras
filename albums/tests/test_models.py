import pytest
from ..models import Album,Song
from artists.models import Artist
from datetime import datetime
from rest_framework.test import APIClient
pytestmark = pytest.mark.django_db

class TestAlbums:
    def test_album_creation_with_missing_data(self):
        artist = Artist()
        artist.stageName = "AnasHagras"
        artist.socialLink = "www.facebook.com/15165156"
        artist.save()
        album = Album()
        album.name = "FirstAlbum"
        album.artist = artist
        album.cost = 2000
        with pytest.raises(Exception):
            album.save()
            
    def test_album_creation_with_correct_data(self):
        artist = Artist()
        artist.stageName = "AnasHagras"
        artist.socialLink = "www.facebook.com/15165156"
        artist.save()
        album = Album()
        album.name = "FirstAlbum"
        album.artist = artist
        album.cost = 2000
        album.releaseDate = datetime.strptime("12/11/2023 09:15:32",  "%d/%m/%Y %H:%M:%S")
        album.save()
        assert len(Album.objects.all()) == 1

    
