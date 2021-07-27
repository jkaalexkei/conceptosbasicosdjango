from django.http import HttpResponse #responde a una peticion de un cliente
from django.http import HttpRequest
from django.shortcuts import render #permite responder a un cliente una peticion mediante un documento html o template renderizado

def index(request):#almacena la peticion y se debe asociar a una url
    
    return HttpResponse('Hola mundo')#retornamos la respuesta 


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


def archivosestaticos(request):
    
    return render(request,'archivosestaticos.html')

def login(request):
    
    return render(request,'usuarios/login.html',{
        
    })