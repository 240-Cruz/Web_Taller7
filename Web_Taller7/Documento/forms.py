from django import forms
from .models import TipoDocumento, Ciudad, Persona

class TipoDocumentoForm(forms.ModelForm):
    class Meta:
        model = TipoDocumento
        fields = ['nombre', 'descripcion']
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control mb-3', 'required':'true', 'id':'nombre'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control mb-3', 'required':'true', 'id':'descripcion'}),
        }

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ['nombre', 'descripcion']
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control mb-3', 'required':'true', 'id':'nombre'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control mb-3', 'required':'true', 'id':'descripcion'}),
        }
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombres', 'apellidos', 'tipo_documento', 'numero_documento', 'lugar_residencia', 'fecha_nacimiento', 'email', 'telefono', 'usuario', 'password']
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'tipo_documento': 'Tipo de documento',
            'numero_documento': 'Número de documento',
            'lugar_residencia': 'Lugar de residencia',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'email': 'Email',
            'telefono': 'Teléfono',
            'usuario': 'Usuario',
            'password': 'Contraseña',
        }
        widgets = {
            'nombres': forms.TextInput(attrs={'class':'form-control mb-3', 'required':'true', 'id':'nombres'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control mb-3', 'required':'true', 'id':'apellidos'}),
            'tipo_documento': forms.Select(attrs={'class':'form-control mb-3', 'required':'true', 'id':'tipo_documento'}),
            'numero_documento': forms.TextInput(attrs={'class':'form-control mb-3', 'required':'true', 'id':'numero_documento'}),
            'lugar_residencia': forms.Select(attrs={'class':'form-control mb-3', 'required':'true', 'id':'lugar_residencia'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type':'date', 'class':'form-control mb-3', 'required':'true', 'id':'fecha_nacimiento'}),
            'email': forms.EmailInput(attrs={'class':'form-control mb-3', 'required':'true', 'id':'email'}),
            'telefono': forms.TextInput(attrs={'class':'form-control mb-3', 'required':'true', 'id':'telefono'}),
            'usuario': forms.TextInput(attrs={'class':'form-control mb-3', 'required':'true', 'id':'usuario'}),
            'password': forms.PasswordInput(attrs={'class':'form-control mb-3', 'required':'true', 'id':'password'}),
        }