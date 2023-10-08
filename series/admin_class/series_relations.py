from series.models.series_relations import SerieRelation
from django.contrib import admin


class SerieRelationAdmin(admin.ModelAdmin):
    model = SerieRelation
    list_display = (
        'id',
        'main',
        'relation',
        'referenced',
    )
    search_fields = ('main', )
    list_filter = ('relation',)