from django.contrib import admin
from hello_world import models

class EventsAdmin(admin.ModelAdmin):
    list_display=['name', 'start_date', 'end_date']

admin.site.register(models.Events, EventsAdmin)

class PeopleAdmin(admin.ModelAdmin):
    list_display=('lname','fname')

admin.site.register(models.People, PeopleAdmin)

