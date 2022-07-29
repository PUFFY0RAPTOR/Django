from django.contrib import admin

from .models import Aprendiz, Monitoria, Actividades

# Register your models here.

@admin.register(Aprendiz)
class AprendizAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'fecha_nacimiento', 'edad_fecha')
    search_fields = ['cedula', 'nombre', 'apellido', 'fecha_nacimiento']

    def edad_fecha(self, obj):
        ed = obj.fecha_nacimiento
        return ed

 
@admin.register(Monitoria)
class MonitoriaAdmin(admin.ModelAdmin):
    list_display = ('cat', 'cedula_Aprendiz', 'aprendiz', 'apellido_Aprendiz', 'fecha_inicio', 'fecha_final')
    search_fields = ['cat', 'aprendiz__nombre', 'aprendiz__apellido', 'aprendiz__cedula']

    def apellido_Aprendiz(self, obj):
        return obj.aprendiz.apellido

    def cedula_Aprendiz(self, obj):
        return obj.aprendiz.cedula


@admin.register(Actividades)
class ActividadesAdmin():
    pass

#admin.site.register(Aprendiz, AprendizAdmin)
#admin.site.register(Monitoria)
#admin.site.register(Actividades)
