from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('authenticate/', views.authenticate),
    path('document/', views.document),
]
