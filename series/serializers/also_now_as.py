from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
# from rest_framework_json_api.relations import ResourceRelatedField

from series.models.also_now_as import AlsoNowAs


class AlsoNowAsSerializer(ModelSerializer):
    class Meta:
        model = AlsoNowAs
        fields = (
            'id',
            'nombre',
        )

    # included_serializers = {
    #     'user': UserSerializer,
    # }
