from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('equipos/', views.lista_equipos, name='lista_equipos'),
    path('equipo/<int:producto_id>/', views.detalle_equipo, name='detalle_equipo'),
]