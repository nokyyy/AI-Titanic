from django.urls import path
from . import views

app_name= 'titanic'
urlpatterns = [
    path('', views.Home, name='home'),
    path('result/', views.Result, name='result'),
]
