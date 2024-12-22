from django.contrib import admin
from .models import *

class PhotInline(admin.TabularInline):
    model = PhotoTours
    extra = 0

class ToursAdmin(admin.ModelAdmin):
    inlines = [PhotInline,]


admin.site.register(Tours,ToursAdmin)
admin.site.register(Carusel)
admin.site.register(Otzyv)