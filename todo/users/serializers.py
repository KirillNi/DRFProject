from rest_framework import serializers
from django.contrib.auth.models import User as AuthUser
from .models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', )


class UserModelSerializerWithSuperuserStaff(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ('username', 'first_name', 'last_name', 'email',
                  'is_superuser', 'is_staff',)
