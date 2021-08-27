from WebAbsensi.models import *
from rest_framework import serializers

# Serializers define the API representation.
class MasterSiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterSiswa
        fields = ['nisn', 'name', 'username', 'password']

class MasterKelasSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterKelas
        fields = ['siswa', 'id_kelas']

class MasterJurusanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterJurusan
        fields = ['siswa', 'id_jurusan']

class AbsensiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absensi
        fields = ['checkin', 'checkout']