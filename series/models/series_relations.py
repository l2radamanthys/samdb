from django.db import models


class SerieRelation(models.Model):
    RELATIONS_CHOICES = (
        ('Secuela', 'Secuela'),
        ('Precuela', 'Precuela'),
        ('Historia Principal', 'Historia Principal'),
        ('Historia Paralela', 'Historia Paralela'),
        ('Historia Completa', 'Historia Completa'),
        ('Resumen', 'Resumen'),
    )

    main = models.ForeignKey("series.Serie", on_delete=models.CASCADE, related_name="series_relations")
    referenced =models.ForeignKey("series.Serie", on_delete=models.CASCADE, related_name="series_relations_referenced")
    relation = models.CharField(max_length=50, choices=RELATIONS_CHOICES, default=None, null=True, blank=True)
    order = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        db_table = 'series_relations'
        verbose_name = "Relacion entre series"
        verbose_name_plural = "Relaciones entre series"

    def __str__(self):
        return f"{self.main} ES ({self.relation}) DE {self.referenced}"
