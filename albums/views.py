from django.shortcuts import render
from albums.models import Album
from artists.models import Artist
from django.http import HttpResponse

def create(request):
    data = {
        'artists' : Artist.objects.all()
    }
    return render(request,"albums/create.html",data)

def store(request):
    if request.method == "POST":
        album = Album()
        album.name = request.POST['name']
        album.releaseDate = request.POST['releaseDate']
        album.cost = request.POST['cost']
        print(Artist.objects.get(id = int(request.POST['artist'])))
        album.artist = Artist.objects.get(id = int(request.POST['artist']))
        album.save()
        if request.method == "POST":
            msg = "item stored successfully"
        else :
            msg = ""
        data = {
            'msg' : msg
        }
        return show(request,data)
    return HttpResponse("Page Not Found")
    

def show(request,msg={'msg':''}):
    data = {
        'albums' : Album.objects.all(),
        'msg' : msg['msg']
    }
    return render(request,"albums/show.html",data)