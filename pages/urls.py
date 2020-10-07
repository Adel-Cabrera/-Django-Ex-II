from django.urls import path

from . import views

# Ruta de las vistas
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about')
]
