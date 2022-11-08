import pytest

pytestmark = pytest.mark.django_db
from ..serializers import AlbumCreateSerializer , AlbumSerializer
from artists.models import Artist
from users.models import User
from ..models import Album
class TestSerializer:
    def test_serializer_success(self,auth_client):
        client,_ = auth_client()
        artist = Artist()
        artist.user = User.objects.get(id=_)
        artist.stageName = "test"
        artist.socialLink = "https://facebook.com/5465"
        artist.save()
        album = AlbumCreateSerializer(data={
            'name' : 'albumTest',
            'cost' : '2000',
            'artist' : '1',
            'releaseDate' : '2022-10-10T20:20:10.4456'
        })
        assert album.is_valid()
        album.save()
        assert album is not None

    def test_serializer_fail(self):
        album = AlbumCreateSerializer(data={
            'name' : 'albumTest',
            'cost' : '2000',
            'artist' : '',
            'releaseDate' : '2022/10/10T20:20:10.4456'
        })
        assert album.is_valid() == False
        album = AlbumCreateSerializer(data={
            'name' : '',
            'cost' : '2000',
            'artist' : '1',
            'releaseDate' : '2022/10/10T20:20:10.4456'
        })
        assert album.is_valid() == False

    def test_deserializer_success(self,auth_client):
        client , _ = auth_client()
        artist = Artist()
        artist.user = User.objects.get(id=_)
        artist.stageName = "test"
        artist.socialLink = "https://facebook.com/5465"
        artist.save()
        album = AlbumCreateSerializer(data={
            'name' : 'albumTest',
            'cost' : '2000',
            'artist' : '1',
            'releaseDate' : '2022-10-10T20:20:10.4456'
        })
        assert album.is_valid()
        album.save()
        album = Album.objects.get(id=1)
        deserializer = AlbumSerializer(instance=album).data
        assert deserializer['name'] == 'albumTest'
        assert deserializer['cost'] == '2000.00'
        assert deserializer['artist']['stageName'] == artist.stageName
        assert deserializer['artist']['socialLink'] == artist.socialLink
