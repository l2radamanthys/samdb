from django.db import models


class AlsoNowAs(models.Model):
    name = models.CharField(max_length=200)
    serie = models.ForeignKey("series.Serie", on_delete=models.CASCADE, related_name="also_now_as")

    class Meta:
        db_table = 'also_now_as'
        verbose_name = "Tambien conocido como"
        verbose_name_plural = "Tambien conocidos como"

    def __str__(self):
        return self.name
