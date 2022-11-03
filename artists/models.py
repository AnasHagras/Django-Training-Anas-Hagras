from django.db import models
from users.models import User
class Artist(models.Model):
    stageName = models.CharField(max_length=50 , unique = True, null = False , blank = False)
    socialLink = models.URLField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    def __str__ (self):
        return self.stageName
    