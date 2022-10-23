from django.shortcuts import render
from django.views import View
class Login(View):
    def get(self,request,*args,**kwargs):
        # handle the auth login 
        return render(request,"authentication/login.html")
    
class Register(View):
    def get(self,request,*args,**kwargs):
        # handle the auth login 
        return render(request,"authentication/register.html")

class Logout(View):
    pass
