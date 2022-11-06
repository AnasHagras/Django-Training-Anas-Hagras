from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from artists.models import Artist
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_congratulation_email
from artists.serializers.ArtistSerializer import ArtistSerializer

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Album(TimeStampedModel):
    name = models.CharField(max_length = 50 , default="New Album")
    releaseDate = models.DateTimeField(null = False)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    artist = models.ForeignKey(Artist,on_delete = models.CASCADE)
    is_approved = models.BooleanField(default = False,
        help_text='Approve the album if its name is not explicit')

    def __str__ (self) :
        return self.name


@receiver(post_save, sender=Album, dispatch_uid="send_email")
def send_email(sender, instance, **kwargs):
    send_congratulation_email.delay(instance.name,ArtistSerializer(instance=instance.artist).data)

class Song(TimeStampedModel):
    name = models.CharField(max_length = 50, default="")
    song_image = models.ImageField(upload_to='songs/photos',default = None)
    song_thumbnail = ImageSpecField(source='song_image',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 100})
    song_audio = models.FileField(upload_to="songs/files")
    album = models.ForeignKey( Album,on_delete = models.CASCADE,default = None)
    def __str__(self):
        return self.name
    
    
    