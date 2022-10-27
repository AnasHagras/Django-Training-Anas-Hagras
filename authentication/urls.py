from django.urls import path

from . import views

urlpatterns = [
    path('login',views.Login.as_view(),name='login'),
    path('register',views.Register.as_view(),name='register'),
    path('loginAction',views.LoginAction.as_view(),name="loginAction"),
    path('registerAction',views.RegisterAction.as_view(),name="registerAction"),
    path('logout',views.Logout.as_view(),name="logout"),
]
