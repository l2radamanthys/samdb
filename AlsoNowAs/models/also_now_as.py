from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'also_now_as'
        verbose_name = "Genre"
        verbose_name_plural = "also_now_as"

    def __str__(self):
        return self.nombre
