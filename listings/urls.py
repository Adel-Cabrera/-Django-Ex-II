from django.urls import path

from . import views

# Ruta de las vistas de listings
# localhost:8080/listings -> definido desde el main urls.py
urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>/', views.listing, name='listing'),
    path('search/', views.search, name='search')

]
