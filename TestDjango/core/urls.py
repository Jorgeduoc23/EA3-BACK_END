from django.urls import path
from .views import home, contacto, vehiculos


urlpatterns = [
    path('' , home,name="home"),
    path('contacto/', contacto , name="contacto"),
    path('vehiculos/', vehiculos, name="vehiculos")
]