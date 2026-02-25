from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('generate/', views.generate_txt_view, name='generate_txt'),
]
