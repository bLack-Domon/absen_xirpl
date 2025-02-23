from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('absensi-kelas/', views.absen, name='absensi'),
]
