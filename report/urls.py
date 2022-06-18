from django.urls import path
from report import views

urlpatterns = [
    path('', views.home, name='home'),
    path('export_text_file', views.export_text_file, name='export_text_file'),
    
]
