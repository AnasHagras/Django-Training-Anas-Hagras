from django.db.models import Count, Q
from django.shortcuts import render

from albums.models import Album
from albums.views import show

from django.core.exceptions import ValidationError

from .models import Artist


def index(request , msg={'msg':''}):
    artists = []
    for artist in Artist.objects.all():
        artists.append({'artist':artist,'albums':Album.objects.filter(Q(artist=artist))})  
    
    # for item in albums[44]:
    #     print(item.name)

    data = {
        'artists' : artists,
        'msg' : msg['msg']
        # 'albums': albums
        # 'albums' : Artist.objects.filter(Q(album__is_approved=True)).annotate(count = Count('album')).order_by('-count')
    }
    if request.method == "POST":
        return render(request,"artists/index.html",data)
    return render(request,"artists/index.html",data)

def create(request , msg = {}):
    return render(request,"artists/create.html",{"msg":msg.items()})

def store(request):
    artist = Artist()
    artist.stageName = request.POST['stageName']
    artist.socialLink = request.POST['socialLink']
    try :
        artist.full_clean()
        artist.save()
        return index(request,{"msg":"Created Successfully!"})
    except ValidationError as err:
        msg = {}
        for e in err :
            msg[e[0]] = e[1]
        return create(request,msg)
