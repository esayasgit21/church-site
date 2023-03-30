from django.contrib import admin

# Register your models here.
from .models import Location, Service, Event
from django.contrib.auth.models import Group

admin.site.register(Service)

# Remove Groups
admin.site.unregister(Group)
#admin.site.register(Event)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'phone')
	ordering = ('name',)
	search_fields = ('name', 'address')
        

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'location', 'event_date', 'description', 'manager', 'approved')
    list_display = ('name', 'event_date', 'location')
    list_filter = ('event_date', 'location')
    ordering = ('event_date',)
