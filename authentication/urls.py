from django.urls import path
from . import views
from knox import views as knox_views
urlpatterns = [
    path('register/',views.Register.as_view(),name="register"),
    path('login/',views.Login.as_view(),name="login"),
    path('logout/',knox_views.LogoutView.as_view(),name="logout")
]
