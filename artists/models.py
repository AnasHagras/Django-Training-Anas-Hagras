from django.db import models

# Create your models here.
class Artist(models.Model):
    stageName = models.CharField(max_length=50 , unique = True, null=False)
    socialLink = models.CharField(max_length=100 )

    def __str__ (self):
        return self.stageName
    