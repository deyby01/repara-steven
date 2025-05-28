from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('sobre-nosotros/', views.sobre_nosotros_view, name='sobre_nosotros'),
    path('contacto/', views.contacto_view, name='contacto'),
    path('reparaciones/', views.reparaciones_view, name='reparaciones'),
]