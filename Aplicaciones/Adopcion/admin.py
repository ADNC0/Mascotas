from django.contrib import admin

# Register your models here.
from .models import Persona, Mascota, Adopcion
# Register your models here.
admin.site.register(Persona)
admin.site.register(Mascota)
admin.site.register(Adopcion)