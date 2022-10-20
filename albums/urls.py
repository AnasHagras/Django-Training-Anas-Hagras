from django.urls import path

from . import views

urlpatterns = [
    path('', views.show),
    path('create',views.create,name="albums/create"),
    path('store' , views.store,name="albums/store"),
    path('show',views.show,name="albums/show")
]
