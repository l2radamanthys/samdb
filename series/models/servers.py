from django.db import models


class Server(models.Model):
    serie = models.ForeignKey("Serie", on_delete=models.CASCADE, related_name="servidores")
    name = models.CharField("Nombre", max_length=100)
    url = models.CharField("URL", max_length=200, default="https://")
    url_format = models.CharField("Formato", max_length=200, default="https://")
    order = models.IntegerField(default=None, blank=True, null=True)

    class Meta:
        db_table = "servers"
        verbose_name = "Servidor"
        verbose_name_plural = "Servidores"
        ordering = ['name']

    def __str__(self):
        return self.name
