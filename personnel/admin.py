from django.contrib import admin
from .models import Person, Team, Country, TeamMember, Driver


class TeamMemberAdmin(admin.TabularInline):
    model = TeamMember
    extra = 1


class TeamAdmin(admin.ModelAdmin):
    fields = (
        ("team_name", "nationality"),
        "team_principal",
        ("driver1", "driver2"),
    )
    inlines = [TeamMemberAdmin]


class PersonAdmin(admin.ModelAdmin):
    fields = (("first_name", "last_name", "nationality"),)


class DriverAdmin(admin.ModelAdmin):
    fields = (
        ("driver", "driver_abbreviation"),
        ("driver_number", "secondary_driver_number"),
    )


# Register your models here.
admin.site.register(Person, PersonAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Country)
