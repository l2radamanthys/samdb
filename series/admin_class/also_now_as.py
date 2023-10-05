from django.contrib import admin
from series.models.also_now_as import AlsoNowAs


class AlsoNowAsAdmin(admin.ModelAdmin):
    model = AlsoNowAs
    list_display = (
        'id',
        'serie',
        'name',
    )

