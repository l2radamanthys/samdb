from django.contrib import admin
from series.admin_class.series import Serie, SerieAdmin
from series.admin_class.also_now_as import AlsoNowAs, AlsoNowAsAdmin
from series.admin_class.genres import Genre, GenreAdmin
from series.admin_class.series_genres import SerieGenre, SerieGenreAdmin
from series.admin_class.servers import Server, ServerAdmin
from series.admin_class.series_relations import SerieRelation, SerieRelationAdmin


admin.site.register(Serie, SerieAdmin)
admin.site.register(AlsoNowAs, AlsoNowAsAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(SerieGenre, SerieGenreAdmin)
admin.site.register(Server, ServerAdmin)
admin.site.register(SerieRelation, SerieRelationAdmin)


