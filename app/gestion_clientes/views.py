from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from app.modelo.models import Cliente, Mascota,Cita
from .forms import ClienteFormulario, MascotaFormulario,FormularioCita
from django.contrib.auth.models import User, Group

@login_required
def index(request):
    usuario = request.user
    grupos = [ x.name for x in usuario.groups.all()]
    if usuario.groups.filter(name = 'gestion_clientes').exists():
        listaCliente = Cliente.objects.all().order_by('apellidos')
        listaMascota = Mascota.objects.all().order_by('nombreMascota')
        listaCitas = Cita.objects.all().order_by('fecha')
        return render(request,'clientes/principal.html', locals())
    else:
        return render(request,'login/aceso_prohibido.html', locals())
    
def crearClientes(request):
    usuario = request.user
    grupos = [ x.name for x in usuario.groups.all()]
    formulario_cliente = ClienteFormulario(request.POST)
    if request.method == 'POST':
        if formulario_cliente.is_valid():
            cliente = Cliente()
            datos_cliente = formulario_cliente.cleaned_data
            cliente.cedula = datos_cliente.get('cedula')
            cliente.nombres = datos_cliente.get('nombres')
            cliente.apellidos = datos_cliente.get('apellidos')
            cliente.direccion = datos_cliente.get('direccion')
            cliente.correo = datos_cliente.get('correo')
            cliente.telefono = datos_cliente.get('telefono')
            cliente.celular = datos_cliente.get('celular')

            cliente.save()
            return redirect(index)
    return render(request, 'clientes/formulario_crear.html', locals())

def crearMascota(request):
    usuario = request.user
    grupos = [ x.name for x in usuario.groups.all()]
    formulario_mascota = MascotaFormulario(request.POST)
    if request.method == 'POST':
        if formulario_mascota.is_valid():
            mascota = Mascota()
            datos_mascota = formulario_mascota.cleaned_data
            mascota.nombreMascota = datos_mascota.get('nombreMascota')
            mascota.edad = datos_mascota.get('edad')
            mascota.tipoMascota = datos_mascota.get('tipoMascota')
            mascota.raza = datos_mascota.get('raza')
            mascota.save()
            return redirect(index)
    return render (request,'clientes/crear_mascota.html',locals())

def eliminarCliente(request,id):
    cliente = Cliente.objects.get(id = id)
    cliente.delete()
    return redirect(index)

def eliminarMascota(request,id):
    mascota = Mascota.objects.get(id = id)
    mascota.delete()
    return redirect(index)

def transaccionCita(request):
    usuario = request.user
    grupos = [ x.name for x in usuario.groups.all()]
    formulario_cita = FormularioCita(request.POST)
    if request.method == 'POST':
        if formulario_cita.is_valid():
            datos = formulario_cita.cleaned_data
            cita = Cita()
            cita.fecha = 'fecha'
            cita.nombrePropietario = datos.get('nombrePropietario')
            cita.cedula = datos.get('cedula')
            cita.nombreMascota = (datos.get('nombreMascota'))
            cita.descripcion = datos.get('descripcion')
            cita.save()
            return redirect(index)
    return render (request,'transacciones/transaccionCita.html',locals())