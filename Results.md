>>> from datetime import datetime
>>> from albums.models import Album
>>> from artists.models import Artist

>>> artist1 = Artist(stageName="Anas", socialLink="www.facebook.com/465165165")
>>> artist2 = Artist(stageName="John", socialLink="www.facebook.com/16512136")
>>> artist3 = Artist(stageName="Sandi", socialLink="www.facebook.com/5161612")

>>> artist1.save()
>>> artist2.save()
>>> artist3.save()

>>> query = Artist.objects.all()
>>> print(query)
<QuerySet [<Artist: d>, <Artist: e>, <Artist: f>, <Artist: Anas>, <Artist: John>, <Artist: Sandi>]>

>>> query = Artist.objects.order_by("stageName")
>>> print(query)
<QuerySet [<Artist: Anas>, <Artist: John>, <Artist: Sandi>, <Artist: d>, <Artist: e>, <Artist: f>]>

>>> query = Artist.objects.filter(stageName__startswith="a")
>>> print(query)
<QuerySet [<Artist: Anas>]>

>>> album1 = Album.objects.create(
...     name="Underground Album",
...     releaseDate=datetime(2020,10,15),
...     cost=2000,
...     artist=artist1)
>>> album1.save()
 
>>> album2 = artist2.album_set.create(
...     name="ECPC", 
...     releaseDate=datetime(2022,1,1),
...     cost=1,
...     artist=artist2
... )

>>> query = Album.objects.order_by("releaseDate").first()
>>> print(query)
Underground Album

>>> query = Album.objects.exclude(releaseDate__lte =  datetime.today())
>>> print(query)
<QuerySet []>

>>> query = Album.objects.filter(releaseDate__lte = datetime.today())
>>> print(query)
<QuerySet [<Album: Underground Album>, <Album: ECPC>, <Album: Underground Album>, <Album: ECPC>]>

>>> query = Album.objects.all().count()
>>> print(query)
4

>>> query = artist1.album_set.all()
>>> print(query)
<QuerySet [<Album: Underground Album>]>

>>> query = Album.objects.order_by("cost","name")
>>> print(query)
<QuerySet [<Album: ECPC>, <Album: ECPC>, <Album: Underground Album>, <Album: Underground Album>]>