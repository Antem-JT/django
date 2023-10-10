from django.forms import ModelForm
from .models import Note

class ModelForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text']