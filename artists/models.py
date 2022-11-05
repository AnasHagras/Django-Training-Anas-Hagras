from django.db import models

class Artist(models.Model):
    stageName = models.CharField(max_length=50 , unique = True, null = False , blank = False)
    socialLink = models.URLField(max_length=100)

    def __str__ (self):
        return self.stageName
    