from django.urls import path
from .api import EquipoViewSet
from rest_framework import routers

router=routers.DefaultRouter()

router.register('api/app', EquipoViewSet,'app')
urlpatterns= router.urls