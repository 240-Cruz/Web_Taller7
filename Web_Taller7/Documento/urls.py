from django.urls import path
from . import views
from .CRUD import documentos, ciudades, personas

urlpatterns = [
    path('', views.index, name='index'),
    #PERSONA URLS
    path('Documento/', personas.obtener_personas, name='obtener_personas'),
    path('Documento/crearpersona/', personas.crear_persona, name='crear_persona'),
    path('Documento/actualizarpersona/<int:id>/', personas.actualizar_persona, name='actualizar_persona'),
    path('Documento/eliminarpersona/<int:id>/', personas.eliminar_persona, name='eliminar_persona'),
    #CIUDADES URLS
    path('ciudad/', ciudades.obtener_ciudades, name='obtener_ciudades'),
    path('ciudad/crearciudad/', ciudades.crear_ciudad, name='crear_ciudad'),
    path('ciudad/actualizarciudad/<int:id>/', ciudades.actualizar_ciudad, name='actualizar_ciudad'),
    path('ciudad/eliminarciudad/<int:id>/', ciudades.eliminar_ciudad, name='eliminar_ciudad'),
    #TIPO DOCUMENTO URLS
    path('tipodocumento/', documentos.obtener_documentos, name='obtener_documentos'),
    path('tipodocumento/creardocumento/', documentos.crear_documento, name='crear_documento'),
    path('tipodocumento/actualizardocumento/<int:id>/', documentos.actualizar_documento, name='actualizar_documento'),
    path('tipodocumento/eliminardocumento/<int:id>/', documentos.eliminar_documento, name='eliminar_documento'),
]