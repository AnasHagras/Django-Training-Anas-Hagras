from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from users.models import User
from users.serializers import UserSerializer
# Create your views here.
class UserApi(APIView):
    permission_classes = []
    authentication_classes = []
    def get(self,request,pk,*args,**kwargs):
        try:
            user = User.objects.get(pk=pk)
            return Response(UserSerializer(user).data)
        except User.DoesNotExist:
            return Response(status=404,data="User Not Found")
    def put(self,request,pk):
        if request.user == pk:
            try :
                user = User.objects.get(pk=pk)
                serializer = UserSerializer(user,data = request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response("Updated Successfully!")
                else :
                    return Response("Invalid Data!")
            except :
                return Response("User Not Found!")
        else :
            return Response("You Don't Have Access !")
    def patch(self,request,pk):
        if request.user == pk:
            try :
                user = User.objects.get(pk=pk)
                serializer = UserSerializer(user,data = request.data , partial = True)
                if serializer.is_valid():
                    serializer.save()
                    return Response("Updated Successfully!")
                else :
                    return Response("Invalid Data!")
            except :
                return Response("User Not Found!")
        else :
            return Response("You Don't Have Access !")
    
