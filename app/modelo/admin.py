from django.contrib import admin
from .models import Cita
from .models import Cliente
from .models import Mascota

#Register your models here.
admin.site.register(Cita)
admin.site.register(Cliente)
admin.site.register(Mascota)
    