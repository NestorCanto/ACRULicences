from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from datetime import date, datetime, timedelta
from django.db.models.deletion import CASCADE
from django.utils import timezone

class UserProfileManager(BaseUserManager):
    '''manager para perfiles de usario'''
    def create_user(self,email,name,password=None):
        ''''crear nuevo usuerprofile'''
        if not email:
            raise ValueError('El usuario debe tener un email')
        else:
            email=self.normalize_email(email)
            user=self.model(email=email,name=name)
            user.set_password(password)
            user.save(using=self._db)
            return user

    def  create_superuser(self,email,name,password):
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    '''Modelo bds para usuarios en el sistema'''
    id = models.AutoField(primary_key=True)
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    
    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        '''obtener nombre completo el usuario'''
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        '''retornar cadena representando el usuario'''
        return self.email



""" modelos de cliente, producto y lisencias-------------------------------------------- """
CHOICES = (
    ("On-premise", "On-premise"),
    ("Cloud", "Cloud"),
)
class Client(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre= models.CharField(max_length=200)
    Epicor_version= models.CharField(max_length=50)
    Epicor_type= models.CharField(max_length=50, choices = CHOICES,
        default = 'Cloud')
    Activo= models.BooleanField(default=True)
    Creado = models.DateTimeField('Fecha de creación')
    Actualizado = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Nombre
    


class Product(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre=models.CharField(max_length=100,default='ACRU')
    Descripcion=models.CharField(max_length=250)
    Creado = models.DateTimeField('Fecha de creación')
    Actualizado = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Nombre
    

#Modelo usuarios (Est podria usarse para autentificar en las licencias en vez del que 
# tra por defecto Dajango, para asi poder tener separado los admins de los product users)

class Usuario(models.Model):
    Nombre=models.CharField(max_length=255)
    Usuario=models.CharField(max_length=255,unique=True)
    Contraseña=models.CharField(max_length=255)
    Creado = models.DateTimeField('Fecha de creación',default=datetime.now())
    Actualizado = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Usuario



#Modelo de lisencias------------------------------------------------------
status = (
    ("InActiva", "InActiva"),
    ("Vigente", "Vigente"),
    ("Vencida", "Vencida"),
)
class Lisence(models.Model):
    #there is a way to get the name of the data of the foreingkey besides the id?
    Cliente=models.ForeignKey(Client, on_delete=models.CASCADE)
    Producto=models.ForeignKey(Product, on_delete=models.CASCADE)
    #Usuario=models.CharField(max_length=100)
    Usuario=models.ForeignKey(Usuario,on_delete=CASCADE)
    Compañía_ERP=models.CharField(max_length=100)
    Estado= models.CharField(max_length=50, choices = status,default="Vigente")
    Fecha_de_inicio = models.DateField('Fecha de inicio')
    Fecha_de_fin = models.DateField('Fecha de fin')  
    Creado = models.DateTimeField('Fecha de creación',default=datetime.now())
    Actualizado = models.DateTimeField(auto_now=True)
    def dias_restantes(self):
        return self.Fecha_de_fin-self.Fecha_de_inicio



