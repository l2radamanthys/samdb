from django.contrib import admin
from series.models.genres import Genre


class GenreAdmin(admin.ModelAdmin):
    model = Genre
    list_display = (
        'id',
        'name',
    )
    search_fields = ('name', )

