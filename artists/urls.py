from django.urls import path
from . import views

urlpatterns = [
    # path('',views.Index.as_view()),
    # path('create',views.Create.as_view(),name="artists/create"),
    # path('store',views.Store.as_view(),name="artists/store"),
    path('artists',views.ArtistsAPI.as_view(),name="artist-api")
]
