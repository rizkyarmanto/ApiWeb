from master.models import *
from rest_framework import viewsets
from master.serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# ViewSets define the view behavior.
class MasterSiswaViewSet(viewsets.ModelViewSet):
    queryset = MasterSiswa.objects.all()
    serializer_class = MasterSiswaSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class MasterKelasViewSet(viewsets.ModelViewSet):
    queryset = MasterKelas.objects.all()
    serializer_class = MasterKelasSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class MasterJurusanViewSet(viewsets.ModelViewSet):
    queryset = MasterJurusan.objects.all()
    serializer_class = MasterJurusanSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class AbsensiViewSet(viewsets.ModelViewSet):
    queryset = Absensi.objects.all()
    serializer_class = AbsensiSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
