from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from series.models.series import Serie
from series.serializers.series import SerieSerializer


class SerieViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = SerieSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
