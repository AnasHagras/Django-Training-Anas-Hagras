from rest_framework import serializers
from ..models import Artist
from users.serializers import UserSerializer

class ArtistSerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Artist
        fields = ("stageName" , "socialLink","user" ,"id")