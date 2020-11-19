from django.contrib import admin
from  .models import Autor, Coleccion,  Comic, Tag

# Register your models here.
admin.site.register(Autor)
admin.site.register(Coleccion)
admin.site.register(Comic)
admin.site.register(Tag)