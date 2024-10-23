from django.shortcuts import render
from rest_framework import viewsets, permissions
from surat.serializer import SuratSerializer, KategoriSerializer, JenisSerializer
from surat.models import (
    Surat, Kategori, Jenis
)

def surat_view(request):
    jenis_surat = request.GET.get('jenis')  # Mengambil nilai dari query string 'jenis'

    # Filter data berdasarkan nilai dari jenis_surat
    if jenis_surat == '1':
        surats = Surat.objects.filter(jenis='1')
        title='Surat Masuk'
    else:
        surats = Surat.objects.filter(jenis='2')
        title='Surat Keluar'
    # data yang dikirim
    context={
        'surat':surats,
        'title':title
    }

    return render(request, 'surat.html', context)
def form_view(request):
    
    jenis_surat = request.GET.get('j')  # Mengambil nilai dari query string 'j'

    # Filter data berdasarkan nilai dari jenis_surat
    if jenis_surat == '1':
        jenis = 1
        title='Surat Masuk'
    else:
        jenis = 2
        title='Surat Keluar'
    context={
        'surat':jenis,
        'title':title
    }
    return render(request, 'form.html', context)


class SuratViewset(viewsets.ModelViewSet):
    permission_classes=[permissions.AllowAny]
    queryset=Surat.objects.all().prefetch_related('kategori')
    serializer_class=SuratSerializer

class KategoriViewset(viewsets.ModelViewSet):
    permission_classes=[permissions.AllowAny]
    queryset=Kategori.objects.all()
    serializer_class=KategoriSerializer

class JenisViewset(viewsets.ModelViewSet):
    permission_classes=[permissions.AllowAny]
    queryset=Jenis.objects.all()
    serializer_class=JenisSerializer
