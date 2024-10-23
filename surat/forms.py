from django import forms
from .models import Surat

class SuratForm(forms.ModelForm):
    class Meta:
        model = Surat
        fields = ['prihal', 'kategori', 'status']
