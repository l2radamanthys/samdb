from django.db import models


class SerieGenre(models.Model):
    serie = models.ForeignKey("series.Serie", on_delete=models.CASCADE, related_name="series_genres")
    genre = models.ForeignKey("series.Genre", on_delete=models.CASCADE, related_name="series_genres")
    order = models.IntegerField(default=1)

    class Meta:
        db_table = 'series_genres'
        verbose_name = "Genero por serie"
        verbose_name_plural = "Generos por series"

    def __str__(self):
        return f"{self.serie} {self.genre}"
