from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login ,logout
from artists import views
from django.shortcuts import redirect

class Login(View):
    def get(self,request,*args,**kwargs):
        try :
            return render(request,"authentication/login.html" , data = kwargs['data'])
        except:
            return render(request,"authentication/login.html")
    def post(self,request,*args,**kwargs):
        return self.get(request,args,kwargs)
            
    
class Register(View):
    def get(self,request,*args,**kwargs):
        return render(request,"authentication/register.html")

class Logout(View):
    def post(self ,request,*args,**kwargs):
        logout(request)
        data = {
            'msg' : 'logged out successfully!'
        }
        return render(request,"artists/index.html",data)
    def get(self,request,*args,**kwargs):
        return self.post(request,args,kwargs)

class LoginAction(View):
    def post(self,request,*args,**kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            data = {
                'msg' : 'Welcome' + user.username
            }
            login(request,user)
            return views.Index.as_view()(request=self.request,data = data)
            # A backend authenticated the credentials
        else:
            data = {
                'msg' : 'Invalid username or password'
            }
            return Login.as_view()(request = self.request, data = data)
            # No backend authenticated the credentials

    

class RegisterAction(View):
    def post(self,request,*args,**kwargs):
        if not request.POST['password'] == request.POST['password2']:
            return render(request,"authentication/register.html",{'msg':'password doesn\'t match'})
        else :
            try :
                User.objects.create_user(username =request.POST['username'],password =request.POST['password'] )
                # return redirect("login",msg={'msg':'Successfully registered!'})
                return render(request,"authentication/login.html",{'msg':'Successfully registered!'})
            except :
                return render(request,"authentication/register.html",{'msg':'Invalid Input'})