from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate




class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField()

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password'
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()

    password = serializers.CharField()

    def validate(self, attrs):

        user = authenticate(
            username=attrs['username'],
            password=attrs['password']
        )

        if not user:
            raise serializers.ValidationError(
                "Invalid Credentials"
            )

        attrs['user'] = user

        return attrs
    
 
 
    
    
