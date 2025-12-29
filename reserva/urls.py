from django.urls import path
from . import views

urlpatterns = [
    path('nueva/', views.crear_reserva, name='crear_reserva'),
]
