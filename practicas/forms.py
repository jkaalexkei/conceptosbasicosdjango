
from django import forms
from django.forms.widgets import TextInput #importamos el modulo para crear formularios


#importamos el modelo User para trabjar y validar campos de tipo usuario

from django.contrib.auth.models import User

class RegistroForm(forms.Form):#clase para crear un formulario mediante una clase
    
    #para manejar los atributos de los elementos del formulario se realiza mediante el parametro widget el cual permite agregarle atributos a los elementos de un formulario, el parametro attrs es un diccionario donde colocaremos dichos atributos
    
    
    username = forms.CharField(required=True,min_length=4,max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Usuario',}))
    
    
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
    
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password' }))
    
    #para mostrar este formulario se debe crerar una instancia en el archivo views de la aplicacion
    
    def clean_username(self):
            #el prefijo clean_ permite validar un campo en especifico

        usuario = self.cleaned_data.get('username')#obtenemos lainformacion del input username

        if User.objects.filter(username=usuario).exists():#consultamos los usuarios en la base de datos para verificar que existe un usuario don dicho username

                raise forms.ValidationError('el usuario ya existe oesta en uso')#en caso que exista un usuario devoolvemos un mensaje de error
        else:
                return usuario #retornamos el nuevo usuario




