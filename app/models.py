from django.db import models

# Create your models here.
class Equipo(models.Model):
    Nombre=models.CharField(max_length=30)
    SerialNumber=models.IntegerField()
    Mensaje=models.TextField(max_length=300,blank=True,null=True)
    Fecha_ultimo_mantenimiento=models.DateField(blank=True,null=True)
    Fecha_estimada_devolución=models.DateField(blank=True,null=True)
    Ubicacion=models.CharField(max_length=30, blank=False, null=True)
    EstadoEquipo= (
        ('En Mantenimeinto','En Mantenimiento'),
        ('Habilitado','Habilitado'),
        ('En Mantenimiento','Dado de baja'),
        ('En Desuso','En Desuso'),
        ('En Prestamo','En Prestamo'),
        )
    Estado = models.CharField(max_length=30, choices=EstadoEquipo)
    def __str__(self):
        return 'Equipo: %s ID: %s Estado: %s' % (self.Nombre,self.SerialNumber, self.Estado)