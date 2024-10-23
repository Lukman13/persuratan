from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class BaseModel(models.Model):
    created_at=models.DateTimeField(default=timezone.now)
    deleted_at=models.DateTimeField(default=timezone.now)
    class Meta:
        abstract=True

class Kategori(BaseModel):
    nama = models.CharField(max_length=200)
    def __str__(self):
        return self.nama
class Jenis(BaseModel):
    nama = models.CharField(max_length=200)
    def __str__(self):
        return self.nama

class Surat(BaseModel):
    prihal = models.CharField(max_length=1000)
    jenis=models.ForeignKey(Jenis, on_delete=models.CASCADE)
    status= models.TextField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.prihal

'* class ContentCreator, varaibel content_creator, private __content_creator *'