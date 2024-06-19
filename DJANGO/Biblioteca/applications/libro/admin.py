from django.contrib import admin

# Register your models here.
from .models import Categoria, Libro 

# Register your models here.

# MUESTRA LOS CAMPOS EN EL ADMIN
class ProductoAdmin(admin.ModelAdmin):
    list_display =(
        'nombre' ,
        
    )

class LibroAdmin(admin.ModelAdmin):
    list_display =(
        'titulo',
       
        
    )




admin.site.register(Categoria , ProductoAdmin )
admin.site.register(Libro , LibroAdmin )