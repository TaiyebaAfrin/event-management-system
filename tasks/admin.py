from django.contrib import admin
from .models import Event, EventDetail,Participant, Category


# Register your models here.
admin.site.register(Event)
admin.site.register(EventDetail)
admin.site.register(Participant)
admin.site.register(Category)
