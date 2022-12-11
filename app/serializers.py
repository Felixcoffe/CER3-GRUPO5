from rest_framework import serializers
from .models import Equipo

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Equipo
        fields=('Nombre','SerialNumber','Mensaje','Fecha_ultimo_mantenimiento','Fecha_estimada_devolución','Ubicacion','Estado')
        read_only_fields=('SerialNumber',)