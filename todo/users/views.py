from rest_framework import mixins, viewsets
from django.contrib.auth.models import User as AuthUser
from .serializers import UserModelSerializer, UserModelSerializerWithSuperuserStaff


class UserModelViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                       mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = AuthUser.objects.all()

    def get_serializer_class(self):
        if self.request.version == '2':
            return UserModelSerializerWithSuperuserStaff
        return UserModelSerializer
