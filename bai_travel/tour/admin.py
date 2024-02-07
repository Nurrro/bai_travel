from django.contrib import admin
from .models import *

class PhotInline(admin.TabularInline):
    model = PhotoTours
    extra = 0

class ToursAdmin(admin.ModelAdmin):
    readonly_fields = ("schetchik_zayavok",)
    inlines = [PhotInline,]


admin.site.register(Tours,ToursAdmin)
admin.site.register(Zayavka)
admin.site.register(Carusel)
admin.site.register(HotTour)
admin.site.register(GalleryImage)
admin.site.register(Otzyv)
admin.site.register(PhotoTours)