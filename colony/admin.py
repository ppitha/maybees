from django.contrib import admin

# Register your models here.
from .models import Apiary, Hive, Colony, Hive_Colony_Map

# Create an admin class, then explicitly register the admin class with the model
class ApiaryAdmin (admin.ModelAdmin):
    list_display = ['name', 'description', 'start_date', 'end_date', '_hives' ]

    def _hives (self, obj):
        return obj.hives.all().count()

admin.site.register(Apiary, ApiaryAdmin)

# Decorator that registers the model with the next class as its admin class
@admin.register (Hive)
class HiveAdmin (admin.ModelAdmin):
    #def apiary_description (obj):
    #    return ("%s" % (obj.name))
    list_display = ['name', 'description', 'apiary_id', 'start_date', 'end_date']
    #apiary_id.short_description = 'Apiary'

class ColonyMapsInline (admin.StackedInline):
    model = Hive_Colony_Map
    extra = 1

@admin.register (Colony)
class ColonyAdmin (admin.ModelAdmin):
    list_display = ['queen_name', 'description', 'parent_id', 'source']
    inlines = [ColonyMapsInline]
