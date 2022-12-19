from django.contrib import admin
from . import models

class PublicSourceInline(admin.TabularInline):
    model = models.PubliclyAvailableData

class NotPublicSourceInline(admin.TabularInline):
    model = models.NotPubliclyAvailableData

class WhereToFindInline(admin.TabularInline):
    model = models.WhereToFind

class ThingsToKnowInline(admin.TabularInline):
    model = models.ThingsToKnow

class DataSetAdmin(admin.ModelAdmin):
    inlines = [PublicSourceInline, NotPublicSourceInline, WhereToFindInline, ThingsToKnowInline]

admin.site.register(models.Guide)
admin.site.register(models.Tool)
admin.site.register(models.DataSet, DataSetAdmin)

# Small objects used in lists
# admin.site.register(models.PubliclyAvailableData)
# admin.site.register(models.NotPubliclyAvailableData)
# admin.site.register(models.WhereToFind)
# admin.site.register(models.ThingsToKnow)