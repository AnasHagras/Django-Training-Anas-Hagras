from django.contrib import admin

from . import models


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name' , 'is_approved','artist' , 'created_at' , 'updated_at')
admin.site.register(models.Album,AlbumAdmin)
