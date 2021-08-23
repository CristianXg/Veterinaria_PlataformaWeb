from django import forms
from app.modelo.models import Cliente, Mascota,Cita

class ClienteFormulario(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["cedula","nombres","apellidos","direccion","correo","telefono","celular"]
        widgets = {
            'cedula': forms.TextInput(attrs={'placeholder':'Ingrese Cédula', 'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'placeholder':'Ingrese Nombres', 'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'placeholder':'Ingrese Apellidos', 'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'placeholder': 'Ingrese Dirección','class': 'form-control', 'rows':'4', 'type':'area'}),
            'correo': forms.TextInput(attrs={'placeholder': 'Ingrese Correo Electrónico', 'class': 'form-control col-md-8', 'type': 'email'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingrese Teléfono','class': 'form-control col-md-8'}),
            'celular': forms.TextInput(attrs={'placeholder': 'Ingrese Celular','class': 'form-control col-md-8'}),
            
        }
        

class MascotaFormulario(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ["nombreMascota","edad","tipoMascota","raza"]
        widgets = {
            'nombreMascota': forms.TextInput(attrs={'placeholder': 'Nombre de tú Mascota', 'class': "form-control"}),
            'edad': forms.TextInput(attrs={'placeholder': 'Años humanos de la Mascota', 'class': "form-control"}),
            'tipoMascota': forms.TextInput(attrs={'placeholder': '¿Que tipo de Mascota es?', 'class': "form-control"}),
            'raza': forms.TextInput(attrs={'placeholder': 'Raza de la Mascota', 'class': "form-control"}),
        }

class FormularioCita(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ["fecha","nombrePropietario","cedula","nombreMascota","descripcion"]