from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from AlsoNowAs.models.also_now_as import Genre
from AlsoNowAs.serializers.also_now_as import GenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = GenreSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
