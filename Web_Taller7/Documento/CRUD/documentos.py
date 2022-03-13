from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template import loader
from ..models import TipoDocumento
from ..forms import TipoDocumentoForm


def obtener_documentos(request):
    tDocumento = TipoDocumento.objects.all()
    template = loader.get_template('documentos/documentos.html')
    context = {
        'tDocumento': tDocumento,
    }
    return HttpResponse(template.render(context, request))

def crear_documento(request):
    if request.method == 'POST':
        form = TipoDocumentoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            tDocumento = TipoDocumento(nombre=nombre, descripcion=descripcion)
            tDocumento.save()
    else:
        form = TipoDocumentoForm()
        return render(request, 'forms/form_template.html', {'form': form})
    return HttpResponseRedirect(reverse('obtener_documentos'))

def actualizar_documento(request, id):
    tDocumento = TipoDocumento.objects.get(id=id)
    if request.method == 'POST':
        form = TipoDocumentoForm(request.POST)
        if form.is_valid():
            tDocumento.nombre = form.cleaned_data['nombre']
            tDocumento.descripcion = form.cleaned_data['descripcion']
            tDocumento.save()
    else:
        form = TipoDocumentoForm(data={'nombre': tDocumento.nombre, 'descripcion': tDocumento.descripcion})
        return render(request, 'forms/form_template.html', {'form': form})     
    return HttpResponseRedirect(reverse('obtener_documentos'))   

def eliminar_documento(request, id):
    if request.method == 'POST':
        tDocumento = TipoDocumento.objects.get(id=id)
        tDocumento.delete()
        return HttpResponse(HttpResponse.status_code)
