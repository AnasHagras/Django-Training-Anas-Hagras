from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('create',views.create,name="artists/create"),
    path('store',views.store,name="artists/store")
]
