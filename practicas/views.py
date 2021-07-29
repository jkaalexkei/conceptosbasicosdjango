from django.forms.forms import Form
from practicas.forms import RegistroForm
from django.http import HttpResponse #responde a una peticion de un cliente
from django.http import HttpRequest
from django.shortcuts import redirect, render #permite responder a un cliente una peticion mediante un documento html o template renderizado
from django.contrib.auth import authenticate, logout #funcion para trabajar con la autenticacion de usuarios
from django.contrib.auth import login,logout #importamos la funcion login de django para establecer una sesion
from django.contrib import messages #permite enviar mensajes del servidor al cliente
from .forms import RegistroForm #importamos la clase RegistroForm del archivo forms.py
from django.contrib.auth.models import User #con esta clase podemos crear nuevos usuarios


def index(request):#almacena la peticion y se debe asociar a una url
    
    return render(request,'index.html')#retornamos la respuesta 

def base(request):
    return render(request,'tpl_base.html')

def saludo(request):
    
    return HttpResponse('Hola soy la funcion saludo en el archivo views')


def Renderizado(request):
    #la funcion render recibe tres argumentos (request, temmplate, diccionario()hace referencia al contexto) mediante se le da respuesta a una peticion de un cliente
    return render(request,'index.html',{
        #contexto --> diccionario{clave:valor}
        #permite pasar valores al template
        #la clave del diccionario se puede usar en el template para mostrar dichos valores
        'mensaje':'mensaje de saludo',
        'numero': 10 + 20,
        'valor_bool':True,
        'lista': [1,2,3,4],
        'diccionario':{'clave':'valor'},
    })

def ListarArticulos(request):
    
    return render(request,'productos.html',{
        'empresa':'tecnologia',
        'productos':[
            {'nombre':'monitor','precio':'200$','estado':True},
            {'nombre':'teclado','precio':'50$','estado':False},
            {'nombre':'mouse','precio':'15$','estado':True},
            {'nombre':'router','precio':'100$','estado':True},
            {'nombre':'disco duro','precio':'90$','estado':False},
            {'nombre':'CD-ROM','precio':'50$','estado':True},
            
        ]
    })

def listadeusuarios(request):
    
    usuarios = User.objects.all()
    
    contexto = {'usuarios':usuarios}
    
    return render(request,'usuarios/listadeusuarios.html',contexto)


def archivosestaticos(request):
    
    return render(request,'archivosestaticos.html')

def login_view(request):
    
    if request.method == 'POST':
        
        usuario = request.POST.get('usuario')#el metodo POST es un diccionario y lo cual hace que se pueda usar el metodo get()
        password = request.POST.get('password')
        
        user = authenticate(username=usuario,password=password)#en caso de existir un usuario la funcion authenticate crea un objeto con ese usuario y se debe alamcenar en una variable en caso contrario retorna none. Una vez verificado esto se puede hacer una condicion para validar dicho usuario y crear esa condicion
        
        if user: #si existe un usuario se crea la sesion
            login(request,user)#la funcion login recibe dos parametros(la peticion almacenada en el request y el usuario almacenado en la variable user)
            # print('usuario autenticado')
            
            messages.success(request,'Bienvenido {}'.format(user.username))#los mensajes admiten dos parametros la peticion request y el mensaje que se va a enviar
            
            return redirect('productos')#redirige a una pagina en particular
        
        else:
            # print('USUARIO NO AUTENTICADO')
            messages.error(request,'usuario no valido')

        
    
    return render(request,'usuarios/loginrefactorizado.html',{
        
        
    })


def iniciarsesion(request):

    if request.method == 'POST':

        usuario = request.POST.get('username')
        clave = request.POST.get('password')
        
        user = authenticate(username=usuario,password=clave)#AUTENTICACION DE USUARIO
        
        if user:#SI HAY UN USUARIO AUTENTICADO
            login(request,user)#SE ESTABLE LA SESION CON EL USUARIO AUTENTICADO
            print('el usuario %s a iniciado sesion' %(usuario))
        else:
            print('Ese usuario no existe... ')
            
    
    
    return render(request,'usuarios/iniciarsesion.html',{
        
        
    })


def logout_view(request):

        logout(request)#la funcion logout recibe como parametro la peticion y esta a su vez se encarga de cerrar la sesion
        messages.success(request,'sesion cerrada exitosamente')#se le informa al usuario que la sesion se ha cerrado
        return redirect('login')#una vez cerrada la sesion redirige al login o pagina principal


"""
def inicio(request):
    
    if request.method == 'POST':
        usu = request.POST.get('username')
        pas = request.POST.get('password')
        
        usuario = authenticate(username = usu, password=pas)
        
        if usuario:
            login(request,usuario)
            messages.success(request,'inicio correcto')
            return redirect('productos')
            
        else:
            messages.error(request,'ocurrio un problema en el inicio de sesión')
    
    return render(request,'usuarios/iniciarsesion.html')
    
    
"""

def registro(request):
    
    formulario = RegistroForm(request.POST or None)# generamos una instancia de la clase registroform y esta tienen sus metodos y propiedades vacios. Dentro de la zona de argumentos se coloca dicha expresion para comprobar que se hallan enviado datos mediante el formulario y esos datos se almacenan en la variable formulario, a su vez dentro de la zona de parametros tambien puede ir un diccionario (clave:valor) con los datos que se vayan a procesar en el formulario. En caso que no hayan datos generados mediante el metodo post se genera un formulario vacio

    #condicionamos si se ha enviado algo en el formulario mediante el metodo post y si el formulario es valido
    if request.method=='POST' and formulario.is_valid(): 
        #asignamos el valor recibido a la variable correspondiente y asi obtener el valor de cada campo mediante el atributo cleaned_data
        """
        username = formulario.cleaned_data.get('username')
        email = formulario.cleaned_data.get('email')
        password = formulario.cleaned_data.get('password')"""
        #para generar un nuevo usuario colocamos la siguiente instruccion la cual genera un objeto de tipo usuario el cual se debe almacenar en una variable
        
        usuario = formulario.save()
        """User.objects.create_user(username,email,password)"""#crea un usuario pero sin permisos de administrador
        
        #validamos si se ha creado el usuario

        if usuario:
            login(request,usuario)#validamos si se ha creado la sesion correspondiente a ese usuario
            messages.success(request,'creado existosamente')#mensaje de confirmacion
            return redirect('listadeusuarios')#redirigimos a una pagina en particular
    
    return render(request,'usuarios/registro.html',{
        
        'form':formulario #agregamos el formulario al contexto
    })
    

def crearusuariosnuevos(request):
    
    formulario = RegistroForm(request.POST or None)
    
    if request.method=='POST' and formulario.is_valid(): 
        
        usuario = formulario.save()#aca se llama al metodo save() del archivo forms.py
        if usuario:
             login(request,usuario)
             messages.success(request,'creado existosamente')
             return redirect('listadeusuarios')
    
    return render(request,'usuarios/registro.html',{

                        'form':formulario})
