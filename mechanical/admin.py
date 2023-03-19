from django.contrib import admin
from mechanical.models import TyreManufacturer, TyreCompound, TeamCar, Engine


class TyreCompoundAdmin(admin.TabularInline):
    model = TyreCompound
    extra = 0


class TyreManufacturerAdmin(admin.ModelAdmin):
    inlines = [TyreCompoundAdmin]


admin.site.register(TyreManufacturer, TyreManufacturerAdmin)
admin.site.register(TeamCar)
admin.site.register(Engine)
