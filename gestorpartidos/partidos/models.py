from django.db import models


class Equipo(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Partido(models.Model):
    fecha = models.DateTimeField()
    local = models.ForeignKey(Equipo, related_name='partidos_como_local')
    visitante = models.ForeignKey(Equipo, related_name='partidos_como_visitante')
    ganador = models.ForeignKey(Equipo, null=True, blank=True, related_name='partidos_ganados')

    def __str__(self):
        return self.local.nombre + ' - ' + self.visitante.nombre
