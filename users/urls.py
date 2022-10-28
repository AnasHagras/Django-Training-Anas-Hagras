from django.urls import path

from .views import UserApi

urlpatterns = [
    path("<int:pk>/" , UserApi.as_view(),name="userApi")
]
