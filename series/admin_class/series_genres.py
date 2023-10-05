from django.contrib import admin
from series.models.series_genres import SerieGenre


class SerieGenreAdmin(admin.ModelAdmin):
    model = SerieGenre
    list_display = (
        'id',
        'order',
        'serie',
        'genre',
    )

