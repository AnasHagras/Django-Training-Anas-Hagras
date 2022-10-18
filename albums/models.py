from datetime import datetime
from django.db import models

from artists.models import Artist

class Album(models.Model):
    name = models.CharField(max_length = 50 , default="New Album")
    creationDate = models.DateTimeField(default=datetime.now())
    releaseDate = models.DateTimeField(null = False)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    artist = models.ForeignKey(Artist,on_delete = models.CASCADE)
    
    def __str__ (self) :
        return self.name