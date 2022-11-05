from django.db.models import Count, Q
from django.shortcuts import render

from albums.models import Album

from django.core.exceptions import ValidationError

from django.views import View

from .models import Artist

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from .serializers.ArtistSerializer import ArtistSerializer

class ArtistsAPI(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = []
    
    def get(self,request,*args,**kwargs):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many = True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = ArtistSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)
    
    
