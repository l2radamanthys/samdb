from django.db import models


class Serie(models.Model):
    STATUS_CHOICES = (
        ('P', 'Proximamente'),
        ('A', 'En Emision'),
        ('F', 'Finalizada')
    )


    TYPES_CHOICES = (
        ('TV', 'TV Show'),
        ('MOVIE', 'Pelicula'),
        ('GAME', 'Video Juegos'),
    )

    name = models.CharField("Nombre", max_length=200)
    code = models.CharField("Codigo", max_length=100, default=None, null=True, blank=True)
    description = models.TextField("Descripción")
    calification = models.FloatField("Calificacion", default=None, blank=True, null=True)
    imdb_calification = models.FloatField("IMDB Calificacion", default=None, blank=True, null=True)
    image = models.ImageField("Portada", upload_to="media/uploads", default='media/uploads/default_image.png')
    release_date = models.DateField(default=None, blank=True, null=True)
    chapters = models.IntegerField("Numero de Capitulos", default=None, blank=True, null=True)
    status = models.CharField("Estado", max_length=1, choices=STATUS_CHOICES)
    type = models.CharField("Tipo", max_length=10, choices=TYPES_CHOICES)

    class Meta:
        db_table = "Series"
        verbose_name = "Serie"
        verbose_name_plural = "Series"
        ordering = ['name', '-id']

    def __str__(self):
        return self.name

    def genres(self):
        list_ = [sg.genre.name for sg in self.series_genres.all()]
        return ", ".join(list_)


