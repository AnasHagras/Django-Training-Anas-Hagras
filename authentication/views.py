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
            })
        except :
            return Response("Invalid Login")


class Register(generics.GenericAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = []
    serializer_class = RegisterSerializer
    lookup_field = User
    def post (self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            username = request.data['username']
            email = request.data['email']
            password = request.data['password']
            password2 = request.data['password2']
        except :
            return Response("All Fields Are Required")
        if password == password2:
            try :
                serializer.is_valid(raise_exception = True)
                user = serializer.save()
                return Response({
                    "user" : UserSerializer(user,context = self.get_serializer_context()).data,
                    "token" : AuthToken.objects.create(user)[1]
                })
            except Exception as e:
                return Response("Validation Error!")
        else :
            return Response("Password Doesn't Match")


