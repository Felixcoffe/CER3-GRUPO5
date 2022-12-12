from django.shortcuts import render
from django.db.models import Q
# Create your views here.


def home(request):
    return render(request,'app/home.html')