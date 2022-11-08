from django.contrib import admin
from django.db.models import Q

from albums.models import Album

from . import models

class ArtistAdmin (admin.ModelAdmin):
    def albums_count(self, obj):
        return Album.objects.filter(Q(artist=obj)).filter(Q(is_approved = True)).count()
    list_display = ('stageName', 'albums_count','user','id')
    fieldsets = (
        (None, {
            'fields': ('stageName', 'socialLink','user')
        }),
    )

admin.site.register(models.Artist, ArtistAdmin)
