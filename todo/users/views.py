from rest_framework import mixins, viewsets

from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserAdminSerializer


class CustomUserViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return CustomUserAdminSerializer
        return CustomUserSerializer