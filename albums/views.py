from django.shortcuts import render
from albums.models import Album,Song
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
        album.artist = Artist.objects.get(id = int(request.POST['artist']))
        album.save()
        msg = "item stored successfully"
        data = {
            'msg' : msg
        }
        return Show.as_view()(request=self.request , data = data)
    def get(self,request):
        return HttpResponse("Page Not Found")
        
class SongIndex(View):
    def get(self,request,*args,**kwargs):
        data = {
            'songs' : Song.objects.all()
        }
        return render(request,"songs/index.html", data)
    def post(self,request,*args,**kwargs):
        data = {
            'songs' : Song.objects.all(),
            'msg' : kwargs['data']['msg']
        }
        return render(request,"songs/index.html", data)

class SongCreate(View):
    def get(self ,request,*args,**kwargs):
        data = {
            'albums' : Album.objects.all()
        }
        return render(request,"songs/create.html" , data)

class SongStore(View):
    def post(self,request,*args,**kwagrs):
        name = request.POST['name']
        album = request.POST['album']
        song_image = ""
        song_audio = ""
        valid = True
        data = {}
        if name == "" :
            valid = False
            data['name'] = 'song name cannot be empty' 
        if album == None:
            valid = False
            data['album'] = 'album field cannot be empty'
        try :
            song_image = request.FILES['song_audio']
            song_audio = request.FILES['song_image']
        except :
            valid = False
            data ['files'] = 'files are required'
        if valid :
            data = {
                'msg' : "Song Added Successfully!"
            }
            song = Song()
            song.name = name 
            song.album = Album.objects.get(id = int(request.POST['album']))
            song.song_image = song_image
            song.song_audio = song_audio
            song.save()
            return SongIndex.as_view()(request=self.request,data=data)
            # return render(request,"songs/index.html",data)
        else :
            data['albums'] = Album.objects.all()
            return render(request,"songs/create.html",data)