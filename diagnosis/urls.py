# diagnosis/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page is at the root URL ("/")
    path('diagnose/', views.diagnose, name='diagnose'),  # Diagnose page
    path('result/', views.result, name='result'), 
]


