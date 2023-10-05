from django.contrib import admin
from AlsoNowAs.models.also_now_as import Genre


class GenreAdmin(admin.ModelAdmin):
    model = Genre
    list_display = (
        'id',
        'nombre',
    )

