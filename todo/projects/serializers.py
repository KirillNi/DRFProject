from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.serializers import UserModelSerializer
from .models import Project, ToDo
from abc import ABC


class UserListingField(serializers.RelatedField, ABC):
    def to_representation(self, value):
        return f'{value.get_username()}'

    def to_internal_value(self, data):
        obj = get_user_model().objects.get(username=data)
        return obj


class ProjectModelSerializer(serializers.HyperlinkedModelSerializer):
    users = UserListingField(many=True, queryset=get_user_model().objects.all())

    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(serializers.HyperlinkedModelSerializer):
    users = UserModelSerializer(read_only=True)

    class Meta:
        model = ToDo
        fields = '__all__'
