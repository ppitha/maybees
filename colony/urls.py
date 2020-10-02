from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('apiary/<int:apiary_id>/', views.apiary_detail, name='apiary_detail'),
    path('hive/<int:hive_id>/', views.hive_detail, name='hive_detail'),
    path('colony/<int:colony_id>/', views.colony_detail, name='colony_detail'),

]