from django.contrib import admin

from .models import Events

class EventsAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'slug')
	class meta:
		model = Events

admin.site.register(Events, EventsAdmin)

# Register your models here.
