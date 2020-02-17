from django.urls import path

from application import views

urlpatterns = [
    path('', views.index, name='index'),
]
