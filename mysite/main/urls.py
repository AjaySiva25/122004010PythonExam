from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('details/', views.Busdeets),
    path('display/', views.display),
    path('create_details/', views.create_deets),
    path('search/', views.search)

]