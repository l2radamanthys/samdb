from django.contrib import admin
from series.models.series import Serie
from series.models.genres import Genre
from series.models.series_genres import SerieGenre
from series.models.also_now_as import AlsoNowAs
from series.models.servers import Server
from series.models.series_relations import SerieRelation


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


class SerieRelationInline(admin.TabularInline):
    model = SerieRelation
    fk_name = 'main'
    autocomplete_fields = [
        "referenced",
    ]
    extra = 0


class GenreListFilter(admin.SimpleListFilter):
    title = "Genero"
    parameter_name = 'genre'

    def lookups(self, request, model_admin):
        queryset = Genre.objects.all()
        return [(g.id, g.name) for g in queryset]

    def queryset(self, request, queryset):
        if self.value() is not None:
            ids = [sg.serie.id for sg in SerieGenre.objects.filter(genre__id=self.value())]
            queryset = queryset.filter(id__in=ids)
        return queryset


class SerieAdmin(admin.ModelAdmin):
    model = Serie
    list_display = (
        'id',
        'name',
        'code',
        'type',
        'genres',
        'pub_day_of_week',
        'chapters',
        'calification',
        'imdb_calification',
        'status',

    )
    inlines = [
        SerieGenreInline,
        AlsoNowAsInline,
        ServerInline,
        SerieRelationInline,
    ]
    search_fields = (
        'name',
    )
    list_filter = (
        'type',
        'status',
        'pub_day_of_week',
        GenreListFilter,
    )

