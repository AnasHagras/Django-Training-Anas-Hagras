from django.urls import path

from . import views

urlpatterns = [
    path('', views.Show.as_view(),name='albums/index'),
    path('create',views.Create.as_view(),name = 'albums/create'),
    path('store' , views.Store.as_view(),name="albums/store"),
]
