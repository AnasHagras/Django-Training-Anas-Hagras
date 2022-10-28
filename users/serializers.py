from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ['id','username','email','bio']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ['id','username','email','password']

    def create(self,validated_data):
        user = User.objects.create_user(validated_data['username'],validated_data['email'],validated_data['password'])
        return user