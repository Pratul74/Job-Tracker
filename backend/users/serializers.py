from rest_framework.serializers import ModelSerializer, ValidationError, CharField
from .models import User

class UserListSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['id', 'email', 'first_name', 'last_name', 'phone_number']

class UserRegisterSerializer(ModelSerializer):
    password2=CharField(write_only=True)
    class Meta:
        model=User
        fields=['email', 'first_name', 'last_name', 'password', 'password2']
        extra_kwargs={
            'password':{'write_only': True},
        }
    def validate(self, data):
        if data['password']!=data['password2']:
            raise ValidationError("Password must be same")
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        password=validated_data.pop('password')
        return User.objects.create_user(
            password=password,
            **validated_data
        )