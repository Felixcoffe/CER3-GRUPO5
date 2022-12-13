from .models import Equipo
from rest_framework import viewsets, permissions
from .serializers import EquipoSerializer


class EquipoViewSet(viewsets.ModelViewSet):
    queryset= Equipo.objects.all()
    permission_class=[permissions.AllowAny]
    serializer_class=EquipoSerializer