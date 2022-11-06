from rest_framework import serializers
from .models import Album
from artists.serializers.ArtistSerializer import ArtistSerializer

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=False,read_only=True)
    class Meta :
        model = Album
        fields = ("name" , "artist" , "cost" , "releaseDate" , "is_approved")

class AlbumCreateSerializer(serializers.ModelSerializer):
    class Meta :
        model = Album
        fields = ("name" , "artist" , "cost" , "releaseDate")
    