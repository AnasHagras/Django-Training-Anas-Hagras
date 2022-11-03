from django.urls import path

from . import views

urlpatterns = [
    path('albums/',views.AlbumList.as_view(),name="albums"),
    path('albums/manual',views.AlbumListManual.as_view(),name="albums-manual"),
    path('albums/create/',views.CreateAlbum.as_view(),name="albums-create"),
    # path('albums/', views.Show.as_view(),name='albums/index'),
    # path('albums/create',views.Create.as_view(),name = 'albums/create'),
    # path('albums/store' , views.Store.as_view(),name="albums/store"),
    # path('songs/' , views.SongIndex.as_view(),name="songs/index"),
    # path('songs/create' , views.SongCreate.as_view(),name="songs/create"),
    # path('songs/store' , views.SongStore.as_view(),name="songs/store"),
]
 