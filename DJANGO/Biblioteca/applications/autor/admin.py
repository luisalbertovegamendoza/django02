from django.contrib import admin

from .models import Autor

# Register your models here.

# MUESTRA LOS CAMPOS EN EL ADMIN
class ProductoAdmin(admin.ModelAdmin):
    list_display =(
        'nombre' ,
        'apellido' ,
        'nacionalidad',
        'edad',
    )

   

admin.site.register(Autor , ProductoAdmin)