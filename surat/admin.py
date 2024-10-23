from django.contrib import admin
from surat.models import(
    Kategori,
    Surat,
    Jenis
)
admin.site.register([Kategori, Surat, Jenis])
# Register your models here.
