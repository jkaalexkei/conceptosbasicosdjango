
from django import forms
from django.forms.widgets import TextInput #importamos el modulo para crear formularios


#importamos el modelo User para trabjar y validar campos de tipo usuario

from django.contrib.auth.models import User

class RegistroForm(forms.Form):#clase para crear un formulario mediante una clase
    
    #para manejar los atributos de los elementos del formulario se realiza mediante el parametro widget el cual permite agregarle atributos a los elementos de un formulario, el parametro attrs es un diccionario donde colocaremos dichos atributos
    
    
    username = forms.CharField(required=True,min_length=4,max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Usuario',}))
    
    
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
    
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password' }))
    
    password2 = forms.CharField(label="confirmar password",required=True,widget=forms.PasswordInput(attrs={'class':'form-control', }))
    
    #para mostrar este formulario se debe crerar una instancia en el archivo views de la aplicacion
    
    def clean_username(self):
            #el prefijo clean_ permite validar un campo en especifico

        usuario = self.cleaned_data.get('username')#obtenemos lainformacion del input username

        if User.objects.filter(username=usuario).exists():#consultamos los usuarios en la base de datos para verificar que existe un usuario don dicho username

                raise forms.ValidationError('el usuario ya existe oesta en uso')#en caso que exista un usuario devoolvemos un mensaje de error
        else:
                return usuario #retornamos el nuevo usuario    
        
    def clean_email(self):
            email = self.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                    raise forms.ValidationError('el correo ya existe')
            else:
                    return email

    def clean(self):#se sobreescribe el metodo clean si y solo si necesitamos validar campos que dependan uno de otros como es el caso que el campo password2 depende del password 
            cleaned_data = super().clean() #obtenemos todos los campos del formulario mediante la funcion super
            
            #aca validamos si ambos campos del password coinciden
            if cleaned_data.get('password2') != cleaned_data.get('password'):
                    
                    self.add_error('password2','el password no coincide')#agregamos un error mediante el metodo add_error el cual recibe dos argumentos. el nombre del elemento al que queremos hacer referencia y el mensaje de error que se le pondra
                            
    
    #delegar la posibilidad de crear nuevos usuarios al formulario
    
    def save(self):#usamos el metodo 
            
           return User.objects.create_user(
                    self.cleaned_data.get('username'),
                    self.cleaned_data.get('email'),
                    self.cleaned_data.get('password'),
            )





