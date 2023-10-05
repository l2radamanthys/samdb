from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from series.models.also_now_as import AlsoNowAs
from series.serializers.also_now_as import AlsoNowAsSerializer


class AlsoNowAsViewSet(viewsets.ModelViewSet):
    queryset = AlsoNowAs.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = AlsoNowAsSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
