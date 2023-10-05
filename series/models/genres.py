from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default=None, null=True, blank=True)
    order = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        db_table = 'genres'
        verbose_name = "Genero"
        verbose_name_plural = "Generos"
        ordering = ['-order', 'name', '-id']

    def __str__(self):
        return self.name
