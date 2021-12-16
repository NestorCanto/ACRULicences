import json
from django import views
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt 
from django.shortcuts import render
from rest_framework.decorators import api_view
import json
#modelos
from .models import Client
from .models import Product
from .models import Lisence
from .models import UserProfile
from .models import Usuario
from django.views import View
# Create your views here.

#clients view-------------------------------------------------------------------------------
class ClientView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#Metodo get
    def get(self,request,id=0):
        #es para sacar cuando se quiere solo un dato en la lista
        if(id>0):
            clients=list(Client.objects.filter(Id=id).values())
            if len(clients)>0:
                client=clients[0]
                datos={'message':"Success",'client':client}
            else:
                datos={'message':"Oops, no client aviable..."}
            return JsonResponse(datos)
        else:
            #Muestra todos los datos disponibles
            clients=list(Client.objects.values())
            if len(clients)>0:
                datos={'message':"Success",'clients':clients}
            else:
                datos={'message':"Oops, no clients aviable..."}
            return JsonResponse(datos)
#metodo Post
    def post(self,request):
        #print(request.body)
        jd=json.loads(request.body.decode('utf-8'))
        #print(jd)
        #en teoria asi se guardan los datos, se le pasa el nombre de la posicion del jd(JsonDictionary) y se iguala al del modelo
        Client.objects.create(Nombre=jd['Nombre'],Epicor_version=jd['Epicor_version']
        ,Epicor_type=jd['Epicor_type'],Activo=jd['Activo'],Creado=jd['Creado'],Actualizado=jd['Actualizado'])
        datos={'message':"Success"}
        return JsonResponse(datos)
#metodo Put
    def put(self,request,id):
        jd=json.loads(request.body.decode('utf-8'))
        clients=list(Client.objects.filter(Id=id).values())
        if len(clients)>0:
            #se crea una variable que se iguale a los objetos del modelo
            #y se iguala al id que se le pasa
            client=Client.objects.get(Id=id)
            #Se le pasan los datos de json actualizado a los datos que estaba antes
            client.Nombre=jd['Nombre']
            client.Epicor_version=jd['Epicor_version']
            client.Epicor_type=jd['Epicor_type']
            client.Activo=jd['Activo']
            client.Creado=jd['Creado']
            client.Actualizado=jd['Actualizado']
            client.save()
            datos={'message':"Success"}
        else:
            datos={'message':"Oops, no client aviable..."}
        return JsonResponse(datos)
#Metodo Delete
    def delete(self,request):
        pass



#Products view--------------------------------------------------------------------------
class ProductView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self,request,id=0):#nota: es importante que el id sea igualado a 0
        #es para sacar cuando se quiere solo un dato en la lista
        if(id>0):
            products=list(Product.objects.filter(Id=id).values())
            if len(products)>0:
                products=products[0]
                datos={'message':"Success",'products':products}
            else:
                datos={'message':"Oops, no product aviable..."}
            return JsonResponse(datos)
        else:
            #Muestra todos los datos disponibles
            products=list(Product.objects.values())
            if len(products)>0:
                datos={'message':"Success",'products':products}
            else:
                datos={'message':"Oops, no product aviable..."}
            return JsonResponse(datos)
#Lisences view-------------------------------------------------------------------------------
class LisencesView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
       #es para sacar cuando se quiere solo un dato en la lista
        if(id>0):
            lisences=list(Lisence.objects.filter(id=id).values())
            if len(lisences)>0:
                lisences=lisences[0]
                datos={'message':"Success",'lisences':lisences}
            else:
                datos={'message':"Oops, no lisence aviable..."}
            return JsonResponse(datos)
        else:
            #Muestra todos los datos disponibles
            lisences=list(Lisence.objects.values())
            if len(lisences)>0:
                datos={'message':"Success",'lisences':lisences}
            else:
                datos={'message':"Oops, no lisence aviable..."}
            return JsonResponse(datos)
#UsersProfile view --------------------------------------------------------------
class UsersView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        users=list(UserProfile.objects.values())
        if len(users)>0:
            datos={'message':"Success",'users':users}
        else:
            datos={'message':"Oops, no users aviable..."}
        return JsonResponse(datos)


#User to check view----------------------------------------------------------------------------
class UserCheckView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
       #es para sacar cuando se quiere solo un dato en la lista
        if(id>0):
            usuarios=list(Usuario.objects.filter(id=id).values())
            if len(usuarios)>0:
                usuarios=usuarios[0]
                datos={'message':"Success",'usuarios':usuarios}
            else:
                datos={'message':"Oops, no user aviable..."}
            return JsonResponse(datos)
        else:
            #Muestra todos los datos disponibles
            usuarios=list(Usuario.objects.values())
            if len(usuarios)>0:
                datos={'message':"Success",'usuarios':usuarios}
            else:
                datos={'message':"Oops, no user aviable..."}
            return JsonResponse(datos)
