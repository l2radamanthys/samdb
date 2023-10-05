from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from series.models.servers import Server
from series.serializers.servers import ServerSerializer


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ServerSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
