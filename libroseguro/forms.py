from django import forms
from .models import Libro,Editorial,Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model=Autor
        fields=[
            'nombre',
            'fecha',
        ]
        labels={
            'nombre':'Nombre del Autor:',
            'fecha':'Fecha Pubicación:',
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'fecha': forms.DateField(),
        }

class EditorialForm(forms.ModelForm):
    class Meta:
        model=Editorial
        fields=[
            'nombre',
        ]
        labels={
            'nombre':'Nombre de Editorial',
        }


class LibroForm(forms.ModelForm):
    class Meta:
        model=Libro
        fields=[
            'isbn',
            'titulo',
            'autor',
            'editorial',
            'precio',
         ]
        labels={
            'isbn':'Numero_Libro',
            'titulo':'Titulo Libro',
            'autor':'Nombre del Autor',
            'editorial':'Nombre de la Editorial',
            'precio':'Valor del Libro',
        }
        widgets={
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'editorial': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
        }