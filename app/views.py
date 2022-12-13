from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from app.models import Equipo

def home(request):
    busqueda = request.GET.get("buscar")
    equipos = Equipo.objects.all()
    return render(request,'app/home.html',{"e":equipos},)