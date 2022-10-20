from django.db import models
from django.utils import timezone
from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.models import StatusModel

from artists.models import Artist

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