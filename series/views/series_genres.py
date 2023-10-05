from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from series.models.series_genres import SerieGenre
from series.serializers.series_genres import SerieGenreSerializer


class SerieGenreViewSet(viewsets.ModelViewSet):
    queryset = SerieGenre.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = SerieGenreSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
