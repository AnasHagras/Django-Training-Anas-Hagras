from django.db import models
from django.utils import timezone

from artists.models import Artist


class Album(models.Model):

    name = models.CharField(max_length = 50 , default="New Album")
    creationDate = models.DateTimeField(default = timezone.now)
    releaseDate = models.DateTimeField(null = False)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    artist = models.ForeignKey(Artist,on_delete = models.CASCADE)
    is_approved = models.BooleanField(default = False,
    help_text='Approve the album if its name is not explicit')

    def __str__ (self) :
        return self.name