from django.urls import path, include
from surat.views import surat_view, form_view, SuratViewset, KategoriViewset, JenisViewset
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('jenis', JenisViewset)
router.register('surat', SuratViewset)
router.register('kategori', KategoriViewset)
urlpatterns = [
    path('suratMasuk/', surat_view, name='suratMasuk'),
    path('suratKeluar/', surat_view, name='suratKeluar'),
    path('form/', form_view, name='formSurat'),
    path('api/', include(router.urls))
]