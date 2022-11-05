from django.shortcuts import render
from albums.models import Album,Song
from artists.models import Artist
from django.http import HttpResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AlbumSerializer,AlbumCreateSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from .filters import AlbumFilter
from .tasks import add
class AlbumList(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Album.objects.filter(is_approved=True)
    filterset_class = AlbumFilter
    serializer_class = AlbumSerializer

class AlbumListManual(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = AlbumSerializer
    def get_queryset(self):
        query = Album.objects.filter(is_approved=True)
        try :
            query = query.filter(name__iexact = self.request.GET['name'])
        except:
            pass
        try:
            cost = int(self.request.GET['cost__gte'])
            query = query.filter(cost__gte = cost)
        except KeyError:
            pass
        except:
            raise TypeError("Cost must be integer")
        try :
            cost = int(self.request.GET['cost__lte'])
            query = query.filter(cost__lte = cost)
        except KeyError:
            pass
        except:
            raise TypeError("Cost must be integer")
        return query


class CreateAlbum(generics.CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    serializer_class = AlbumCreateSerializer
    model = Album
        

def CeleryTest(request):
    add.delay()
    return HttpResponse("Done")