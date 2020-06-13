# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('foodmenu/<str:name>/<str:time>/', views.foodmenu, name="foodmenu"),
    path('throw/', views.throw, name="throw"),
    path('catch/', views.catch, name="catch"),
    path('lottobuy/', views.lottobuy, name="lottobuy"),
    path('lottoresult/', views.lottoresult, name="lottoresult"),
    path('artii/', views.artii, name="artii"),
    path('result/', views.result, name="result"),
    
]