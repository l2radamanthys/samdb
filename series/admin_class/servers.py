from django.contrib import admin
from series.models.servers import Server


class ServerAdmin(admin.ModelAdmin):
    model = Server
    list_display = (
        'id',
        'serie',
        'name',
        'url',
    )
    search_fields = (
        'name',
        'url',
    )
    autocomplete_fields = (
        'serie',
    )

