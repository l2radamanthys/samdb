from django.contrib import admin
from series.models.series import Serie
from series.models.series_genres import SerieGenre
from series.models.also_now_as import AlsoNowAs
from series.models.servers import Server


class SerieGenreInline(admin.TabularInline):
    model = SerieGenre
    autocomplete_fields = [
        "genre",
    ]
    extra = 0


class AlsoNowAsInline(admin.TabularInline):
    model = AlsoNowAs
    extra = 0


class ServerInline(admin.TabularInline):
    model = Server
    extra = 0


class SerieAdmin(admin.ModelAdmin):
    model = Serie
    list_display = (
        'id',
        'name',
        'type',
        'genres',
        'chapters',
        'calification',
        'imdb_calification',
        'status',

    )
    inlines = [
        SerieGenreInline,
        AlsoNowAsInline,
        ServerInline
    ]
    search_fields = (
        'name',
    )
    list_filter = (
        'type',
        'status',
    )

