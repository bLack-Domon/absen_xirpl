from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    ambil_data = Siswa.objects.all()

    wadah = {
        'judul': 'Data Siswa XI RPL',
        'menu': 'home',
        # 'data_siswa': Siswa.objects.all()
        'data_siswa': ambil_data
    }
    return render(request, 'index.html', wadah)


def absen(request):
    wadah = {
        'judul': 'Absensi Siswa XI RPL',
        'menu': 'absensi',
        'absen': Absensi.objects.all()
    }
    return render(request, 'absen.html', wadah)