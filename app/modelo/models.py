from django.db import models

class Cliente(models.Model):

    id = models.AutoField(primary_key = True)
    cedula = models.CharField(max_length = 10, unique = True, null = False)
    nombres = models.CharField(max_length = 70, null = False)
    apellidos = models.CharField(max_length = 70, null = False)
    direccion = models.TextField(max_length = 200)
    #estadoCivil = models.CharField(max_length = 15,choices = listaEstadoCivil, null = False, default = "soltero")
    correo = models.EmailField(max_length = 105, null = False)
    telefono = models.CharField(max_length = 15)
    celular = models.CharField(max_length = 15, null = False)
    
    date_created = models.DateTimeField(auto_now_add = True,null = True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        cadena = str(self.cedula)+";"+str(self.nombres)+ ";"+str(self.apellidos)
        return cadena

class Mascota(models.Model):

    id = models.AutoField(primary_key = True)
    nombreMascota = models.CharField(max_length = 40 , null = False)
    edad = models.CharField(max_length = 3 , null = False)
    tipoMascota = models.CharField(max_length = 30,null = False)
    raza = models.CharField(max_length = 20,null = False)

    date_created = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        cadena = str(self.nombreMascota) + ";" + str(self.tipoMascota)+";"+str(self.edad)
        return cadena

class Cita(models.Model):
    
    id = models.AutoField(primary_key = True)
    fecha = models.CharField(max_length = 20, null = False)
    nombrePropietario = models.CharField(max_length = 40 , null = False)
    cedula = models.CharField(max_length = 10, unique = True, null = False)
    nombreMascota = models.CharField(max_length = 40 , null = False)
    descripcion = models.TextField(default = 'Descripción de la Cita')
    
    date_created = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
