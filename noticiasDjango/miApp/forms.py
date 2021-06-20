from django import forms
from django.forms import widgets
from .models import Noticias

class NoticiaForm(forms.ModelForm):

    class Meta:
        model = Noticias
        fields = '__all__'

        widgets = {
            "fechaNoticia": forms.SelectDateWidget(),
            "descripcioLarga": forms.Textarea,
        }    
