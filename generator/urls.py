from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('generate/', views.generate_pdf_view, name='generate_pdf'),
]
