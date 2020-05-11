from __future__ import unicode_literals
from django.db import models
from karyawan.models import Karyawan

# Create your models here.
class Kehadiran (models.Model):
    JENIS_KEHADIRAN_CHOICES = (
        ('izin', 'Izin'),
        ('cuti', 'Cuti'),
        ('alpha', 'Tanpa Alasan'),
        ('hadir', 'Hadir'),
    )

    karyawan = models.ForeignKey(Karyawan, on_delete=models.PROTECT)
    jenis_kehadiran = models.CharField(max_length=20, choices=JENIS_KEHADIRAN_CHOICES)
    waktu = models.DateField()

    def __unicode__(self):
        return self.karyawan.nama
