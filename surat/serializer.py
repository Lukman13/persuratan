from rest_framework import serializers
from surat.models import Surat, Kategori, Jenis

class SuratSerializer(serializers.ModelSerializer):
    # potongan_berita=serializers.SerializerMethodField(read_only=True)
    # tag_str=serializers.SerializerMethodField(read_only=True)
    class Meta:
        exclude=['deleted_at']
        model=Surat
    # def get_potongan_berita(self, obj):
    #     if len(obj.content)>20:
    #         return obj.content[0:20]
    #     return obj.content
    
    # def get_tag_str(self, obj):
    #     if obj.tag.all().exists():
    #         return(tag.nama for tag in obj.tag.all())
    #     return []

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        exclude=['deleted_at']
        model=Kategori

class JenisSerializer(serializers.ModelSerializer):
    class Meta:
        exclude=['deleted_at']
        model=Jenis