from django.db import models

class Siswa(models.Model):
    nama = models.CharField(max_length=100)
    jurusan = models.CharField(max_length=50, default="rpl")
    foto = models.ImageField(upload_to='foto_siswa/', blank=True, null=True)
    qrcode = models.ImageField(upload_to='qrcodes/', blank=True, null=True)

    def __str__(self):
        return self.nama

class Absensi(models.Model):
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    tanggal_absen = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.siswa.nama} - {self.tanggal_absen}"
