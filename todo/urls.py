from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_item/', views.addItem, name='add_item')
]