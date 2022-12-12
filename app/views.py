from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from app.models import Equipo

def home(request):
    busqueda = request.GET.get("buscar")
    equipos = Equipo.objects.all()
    if busqueda:
        equipos = Equipo.objects.filter(
                Q(Estado = busqueda)
            ).distinct()
    return render(request,'app/home.html',{"equi":equipos})