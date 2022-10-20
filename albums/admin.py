from django.contrib import admin

from . import models


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields= ('creationDate',)
    list_display = ('name' , 'is_approved','artist')
    
    
admin.site.register(models.Album,AlbumAdmin)
