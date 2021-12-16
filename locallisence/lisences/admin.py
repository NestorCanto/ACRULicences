from django.contrib import admin
from lisences import models


class lisenceAdmin(admin.ModelAdmin):
     list_display = ('Cliente','Usuario','Fecha_de_inicio', 'dias_restantes','Creado','Actualizado') 
     list_filter = ['Fecha_de_inicio','Cliente']
     #search_fields = ['Usuario','Compañía_ERP']


class PrductAdmin(admin.ModelAdmin):
    list_display = ('Nombre','Creado','Actualizado')
    list_filter = ['Creado','Nombre']

class ClienttAdmin(admin.ModelAdmin):
    list_display = ('Nombre','Epicor_version','Creado','Actualizado')
    list_filter = ['Creado','Epicor_version']

class UserAdmin(admin.ModelAdmin):
    list_display = ('Nombre','Usuario','Creado','Actualizado')
    list_filter = ['Creado']


admin.site.register(models.UserProfile)
admin.site.register(models.Client,ClienttAdmin)
admin.site.register(models.Product,PrductAdmin)
admin.site.register(models.Lisence,lisenceAdmin)
admin.site.register(models.Usuario,UserAdmin)
# Register your models here.
