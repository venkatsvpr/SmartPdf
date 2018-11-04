from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'form'),
    path('complete', views.complete, name = 'complete'),
]