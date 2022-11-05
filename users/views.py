from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from users.models import User
from users.serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import UserPermission

class UserApi(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated|UserPermission]
    def get(self,request,pk,*args,**kwargs):
        try:
            user = User.objects.get(pk=pk)
            return Response(UserSerializer(user).data)
        except User.DoesNotExist:
            return Response(status=404,data="User Not Found")
    def put(self,request,pk):
        try :
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Updated Successfully!",status=201)
            else :
                return Response("Invalid Data!",status=400)
        except :
            return Response("User Not Found!",status=404)
    def patch(self,request,pk):
        try :
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user,data = request.data , partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response("Updated Successfully!",status=201)
            else :
                return Response("Invalid Data!",status=400)
        except :
            return Response("User Not Found!",status=404)
    
