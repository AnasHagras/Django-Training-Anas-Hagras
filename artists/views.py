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

class Index(View):
    def getData(self ,*args, **kwargs):
        artists = []
        for artist in Artist.objects.all():
            artists.append({'artist':artist,'albums':Album.objects.filter(Q(artist=artist))})  
        
        # for item in albums[44]:
        #     print(item.name)

        data = {
            'artists' : artists,
            'msg' : kwargs['data']
            # 'albums': albums
            # 'albums' : Artist.objects.filter(Q(album__is_approved=True)).annotate(count = Count('album')).order_by('-count')
        }
        return data 
    def post (self,request,*args,**kwargs):
        return render(request,"artists/index.html",self.getData(data = kwargs['data']['msg']))
         
    def get(self,request,*args,**kwargs):
        return render(request,"artists/index.html",self.getData(data = ''))

class Create(View):
    def get(self ,request,*args , **kwargs):
        if request.user.is_authenticated:
            try :
                return render(request,"artists/create.html",{"msg":kwargs['msg'].items()})
            except :
                return render(request,"artists/create.html")
        else :
            return render(request,"authentication/login.html",{"msg":"Please Login First"})      
            
    def post(self,request,*args,**kwargs):
        if request.user.is_authenticated :
            return render(request,"artists/create.html",{"msg":kwargs['data'].items()})
        else :
            return render(request,"authentication/login.html",{"msg":"Please Login First"})      
class Store(View):
    def post(self,request,*args , **kwargs):
        artist = Artist()
        artist.stageName = request.POST['stageName']
        artist.socialLink = request.POST['socialLink']
        try :
            artist.full_clean()
            artist.save()
            return Index.as_view()(request = self.request ,data={"msg":"Created Successfully!"})
            # return index(request,{"msg":"Created Successfully!"})
        except ValidationError as err:
            msg = {}
            for e in err :
                msg[e[0]] = e[1]
            return Create.as_view()(request =self.request, data=msg)
            # return create(request,msg)
    def get(request,*args,**kwargs):
        return HttpResponse("Page Not Found")
        
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
    
    
