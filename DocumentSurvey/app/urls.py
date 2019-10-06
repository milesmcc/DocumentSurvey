from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('authenticate/', views.authenticate),
    path('upload/', views.upload),
    path('document/', views.document),
]
