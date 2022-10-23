from django.shortcuts import render
from albums.models import Album
from artists.models import Artist
from django.http import HttpResponse
from django.views import View

class Show(View):
        
    def get(self , request , **kwargs):
        data = {
            'albums' : Album.objects.filter(is_approved=True),
        }
        return render(request,"albums/show.html",data)
    def post (self,request,**kwargs):
        data = {
            'albums' : Album.objects.filter(is_approved=True),
            'msg' : kwargs['data']['msg']
        }
        return render(request,"albums/show.html",data)

class Create(View):
    def get(self,request):
        data = {
            'artists' : Artist.objects.all()
        }
        return render(request,"albums/create.html",data)

class Store(View):
    def post(self,request):
        album = Album()
        album.name = request.POST['name']
        album.releaseDate = request.POST['releaseDate']
        album.cost = request.POST['cost']
        # print(Artist.objects.get(id = int(request.POST['artist'])))
        album.artist = Artist.objects.get(id = int(request.POST['artist']))
        album.save()
        msg = "item stored successfully"
        data = {
            'msg' : msg
        }
        return Show.as_view()(request=self.request , data = data)
    def get(self,request):
        return HttpResponse("Page Not Found")
        