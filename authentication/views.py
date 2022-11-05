from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,authentication, permissions
from users.models import User
from users.serializers import RegisterSerializer,UserSerializer
from json import JSONEncoder,JSONDecoder
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken

class Login(KnoxLoginView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (permissions.AllowAny,)
    def post (self,request):
        serializer = AuthTokenSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception = True)
            user = serializer.validated_data['user']
            token = AuthToken.objects.create(user)
            login(request,user)
            print(request.user)
            return Response({
                'token' : token[1],
                'user' : UserSerializer(user).data
            },status=200)
        except :
            return Response("Invalid Login",status=403)


class Register(generics.GenericAPIView):

    permission_classes = []
    serializer_class = RegisterSerializer
    lookup_field = User
    def post (self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        print("Before")
        return Response({
            "user" : UserSerializer(user,context = self.get_serializer_context()).data,
            "token" : AuthToken.objects.create(user)[1]
        },status=200)
        # try :
            
        # except:
        #     return Response("Validation Error!" , status=400)
        # try:
        #     username = request.data['username']
        #     email = request.data['email']
        #     password = request.data['password']
        #     password2 = request.data['password2']
        # except :
        #     return Response("All Fields Are Required",status=400)
        # if password == password2:
        #     try :
                
        #     except Exception as e:
        #         return Response("Validation Error!",status=400)
        # else :
        #     return Response("Password Doesn't Match",status=400)


